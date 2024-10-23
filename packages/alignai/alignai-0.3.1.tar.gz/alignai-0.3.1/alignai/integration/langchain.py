from __future__ import annotations

import importlib
from datetime import datetime
from importlib import metadata as importlib_metadata
from typing import TypedDict

from packaging import version

from alignai import AlignAI
from alignai.constants import DEFAULT_ASSISTANT_ID, ROLE_ASSISTANT, ROLE_USER
from alignai.utils import CustomProperties

try:
    langchain = importlib.import_module("langchain")
    langchain_version = importlib_metadata.version("langchain")
    if version.parse(langchain_version) < version.parse("0.0.221"):
        raise ImportError("You must install langchain>=0.0.221 to use Align AI integrated ChatMessageHistory.")

    BaseChatMessageHistory = importlib.import_module("langchain.schema").BaseChatMessageHistory
    message_schema = importlib.import_module("langchain.schema.messages")
    BaseMessage, HumanMessage, AIMessage = (
        message_schema.BaseMessage,
        message_schema.HumanMessage,
        message_schema.AIMessage,
    )
except ModuleNotFoundError:
    raise ImportError("You must install 'langchain' to use Align AI integrated ChatMessageHistory.")


class UserInfo(TypedDict):
    display_name: str | None
    email: str | None
    ip: str | None
    country_code: str | None
    create_time: datetime | None
    custom_properties: CustomProperties | None


class ChatMessageHistory(BaseChatMessageHistory):
    def __init__(
        self,
        history_backend: BaseChatMessageHistory,
        sdk: AlignAI,
        session_id: str,
        user_id: str,
        assistant_id: str = DEFAULT_ASSISTANT_ID,
        user_info: UserInfo | None = None,
    ):
        """Initialize Align AI integrated ChatMessageHistory. When initialized, open_session event is emitted.

        Args:
            history_backend (BaseChatMessageHistory): Chat message history backend from LangChain. Reference: https://python.langchain.com/docs/modules/memory/chat_messages/
            sdk (AlignAI): Align AI SDK Instance.
            session_id (str): Session ID.
            user_id (str): User ID.
            assistant_id (str, optional): Assistant ID. Defaults to 'DEFAULT'.
            user_info (UserInfo | None, optional): Providing at least one user information will trigger identify_user event upon initialization. Defaults to None.
        """  # noqa: E501
        self.backend = history_backend
        self.sdk = sdk
        self.session_id = session_id
        self.user_id = user_id
        self.sdk.open_session(session_id=session_id, user_id=user_id, assistant_id=assistant_id)
        if user_info:
            self.identify_user(
                email=user_info.get("email", None),
                ip=user_info.get("ip", None),
                country_code=user_info.get("country_code", None),
                create_time=user_info.get("create_time", None),
                display_name=user_info.get("display_name", None),
                custom_properties=user_info.get("custom_properties", None),
            )

    def add_message(self, message: BaseMessage) -> None:
        """Add a message to the chat history. If the message is human or assistant message, create_message event will be emitted.

        Args:
            message (BaseMessage): One of HumanMessage, AIMessage, or SystemMessage.
        """  # noqa: E501
        if isinstance(message, (HumanMessage, AIMessage)):
            self.sdk.create_message(
                session_id=self.session_id,
                message_index=self._next_message_idx,
                role=ROLE_USER if isinstance(message, HumanMessage) else ROLE_ASSISTANT,
                content=message.content,
            )
        self.backend.add_message(message)

    def clear(self) -> None:
        """Clear the chat history."""
        self.backend.clear()

    def identify_user(
        self,
        display_name: str | None = None,
        email: str | None = None,
        ip: str | None = None,
        country_code: str | None = None,
        create_time: datetime | None = None,
        custom_properties: CustomProperties | None = None,
    ) -> None:
        """Send identify_user event. The user_id provided upon initialization will be used.

        Args:
            email (str | None, optional): User email address. Defaults to None.
            ip (str | None, optional): User IPv4 address. Provide either ip or country code for user location. If both are given, country code overrides ip. Defaults to None.
            country_code (str | None, optional): User country code in ISO Alpha-2. Provide either ip or country code for user location. If both are given, country code overrides ip. Defaults to None.
            create_time (datetime | None, optional): User creation time. Defaults to None.
            display_name (str | None, optional): User display name. Defaults to None.
            custom_properties (dict[str, str] | None, optional): Custom properties associated with the user. Defaults to None.
        """  # noqa: E501
        self.sdk.identify_user(
            user_id=self.user_id,
            email=email,
            ip=ip,
            country_code=country_code,
            create_time=create_time,
            display_name=display_name,
            custom_properties=custom_properties,
        )

    def close(self) -> None:
        """Close the Align AI session. Do not send additional message after calling this method."""
        self.sdk.close_session(session_id=self.session_id)

    @property
    def messages(self) -> list[BaseMessage]:
        """Retrieve the chat history.

        Returns:
            list[BaseMessage]: List of messages consisting of one of BaseMessage, HumanMessage, AIMessage, or SystemMessage.
        """  # noqa: E501
        return self.backend.messages

    @property
    def _next_message_idx(self) -> int:
        return len([message for message in self.messages if isinstance(message, (HumanMessage, AIMessage))]) + 1
