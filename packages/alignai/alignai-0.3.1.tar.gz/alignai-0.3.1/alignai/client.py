from __future__ import annotations

import os
import uuid
from datetime import datetime, timezone

from alignai.api_client import APIClient
from alignai.buffer_storage import BufferStorage
from alignai.config import Config
from alignai.constants import (
    DEFAULT_ASSISTANT_ID,
    FEEDBACK_THUMBS_DOWN,
    FEEDBACK_THUMBS_UP,
    ROLE_ASSISTANT,
    ROLE_USER,
    SERVER_BASE_URL,
    EventTypes,
)
from alignai.logger import get_logger
from alignai.proto.ingestion.v1alpha.event_pb2 import Event, EventProperties
from alignai.utils import (
    CustomProperties,
    datetime_to_timestamp,
    serialize_custom_properties,
)
from alignai.validate import (
    ValidationError,
    validate_custom_properties_or_raise,
    validate_session_id_or_raise,
    validate_user_id_or_raise,
)
from alignai.worker import Worker


class AlignAI:
    def __init__(
        self,
        project_id: str | None = None,
        api_key: str | None = None,
        api_host: str | None = None,
        config: Config | None = None,
    ):
        """Initialize the Align AI SDK.

        Args:
            project_id (str | None): Project ID from Align AI. If not provided, SDK will try to retrieve it from environment variable ALIGNAI_PROJECT_ID.
            api_key (str | None): API Key from Align AI. If not provided, SDK will try to retrieve it from environment variable ALIGNAI_API_KEY.
            api_host (str | None, optional): API host for the Align AI ingestion server. If not provided, SDK will try to retrieve it from environment variable ALIGNAI_HOST. Defaults to "https://api.impaction.ai".
            config (Config | None, optional): The configuration of SDK client. If not provided, default configuration will be used. Defaults to None.
        """  # noqa: E501

        self.project_id = project_id or os.getenv("ALIGNAI_PROJECT_ID")
        assert self.project_id is not None
        self.api_key = api_key or os.getenv("ALIGNAI_API_KEY")
        assert self.api_key is not None
        self.api_host = api_host or os.getenv("ALIGNAI_HOST") or SERVER_BASE_URL
        self.config = config or Config()
        self.logger = get_logger("INFO")
        api_client = APIClient(
            api_host=self.api_host,
            api_key=self.api_key,
            api_max_retries=self.config.api_max_retries,
        )
        self.worker = Worker(
            api_client=api_client,
            logger=self.logger,
            flush_interval_ms=self.config.flush_interval_ms,
            flush_batch_size=self.config.flush_batch_size,
        )
        self.buffer_storage = BufferStorage(max_buffer_size=self.config.max_buffer_size)
        self.worker.setup(self.buffer_storage)
        self.worker.start()

    def open_session(
        self,
        session_id: str,
        user_id: str,
        assistant_id: str = DEFAULT_ASSISTANT_ID,
        custom_properties: CustomProperties | None = None,
    ) -> None:
        """Record the initiation of a session.

        Args:
            session_id (str): Session ID.
            user_id (str): User ID associated with the session.
            assistant_id (str, optional): Assistant ID. Defaults to "DEFAULT".
            custom_properties (dict[str, str] | None, optional): Custom properties associated with the session.
                Defaults to None.
        """
        validate_session_id_or_raise(session_id)
        validate_user_id_or_raise(user_id)
        if len(assistant_id) > 64:
            raise ValidationError("assistant_id must be at most 64 characters")
        if custom_properties:
            validate_custom_properties_or_raise(custom_properties)

        session_properties_args = {"session_id": session_id, "user_id": user_id, "assistant_id": assistant_id}
        open_session_event = Event(
            id=uuid.uuid4().hex,
            type=EventTypes.SESSION_OPEN,
            create_time=datetime_to_timestamp(datetime.now(timezone.utc)),
            properties=EventProperties(
                session_properties=EventProperties.SessionProperties(**session_properties_args),
                custom_properties=serialize_custom_properties(custom_properties) if custom_properties else None,
            ),
            project_id=self.project_id,
        )
        self._collect(open_session_event)

    def close_session(self, session_id: str) -> None:
        """Record the end of a session.

        Args:
            session_id (str): Session ID.
        """
        validate_session_id_or_raise(session_id)

        close_session_event = Event(
            id=uuid.uuid4().hex,
            type=EventTypes.SESSION_CLOSE,
            create_time=datetime_to_timestamp(datetime.now(timezone.utc)),
            properties=EventProperties(session_properties=EventProperties.SessionProperties(session_id=session_id)),
            project_id=self.project_id,
        )
        self._collect(close_session_event)

    def identify_user(
        self,
        user_id: str,
        display_name: str | None = None,
        email: str | None = None,
        ip: str | None = None,
        country_code: str | None = None,
        create_time: datetime | None = None,
        custom_properties: CustomProperties | None = None,
    ) -> None:
        """Record a user.

        Args:
            user_id (str): Unique user ID used internally. This ID will be not displayed on dashboard.
            display_name (str | None, optional): User display name shown on dashboard. Defaults to None.
            email (str | None, optional): User email address.
            ip (str | None, optional): User IPv4 address. Provide either ip or country code for user location. If both are given, country code overrides ip. Defaults to None.
            country_code (str | None, optional): User country code in ISO Alpha-2. Provide either ip or country code for user location. If both are given, country code overrides ip. Defaults to None.
            create_time (datetime | None, optional): User creation time. Defaults to None.
            custom_properties (dict[str, str] | None, optional): Custom properties associated with the user. Defaults to None.
        """  # noqa: E501
        validate_user_id_or_raise(user_id)
        if display_name and len(display_name) > 64:
            raise ValidationError("display_name must be at most 64 characters")
        if email and len(email) > 256:
            raise ValidationError("email must be at most 256 characters")
        if country_code and len(country_code) != 2:
            raise ValidationError("country_code must be ISO Alpha-2 code")
        if custom_properties:
            validate_custom_properties_or_raise(custom_properties)

        user_properties_args = {"user_id": user_id}
        if display_name is not None:
            user_properties_args["user_display_name"] = display_name
        if email is not None:
            user_properties_args["user_email"] = email
        if ip is not None:
            user_properties_args["user_ip"] = ip
        if country_code is not None:
            user_properties_args["user_location"] = EventProperties.UserProperties.Location(country_code=country_code)
        if create_time is not None:
            user_properties_args["user_create_time"] = datetime_to_timestamp(create_time)

        identify_user_event = Event(
            id=uuid.uuid4().hex,
            type=EventTypes.USER_RECOGNIZE,
            create_time=datetime_to_timestamp(datetime.now(timezone.utc)),
            properties=EventProperties(
                user_properties=EventProperties.UserProperties(**user_properties_args),
                custom_properties=serialize_custom_properties(custom_properties) if custom_properties else None,
            ),
            project_id=self.project_id,
        )
        self._collect(identify_user_event)

    def create_message(
        self,
        session_id: str,
        message_index: int,
        role: str,
        content: str,
        custom_properties: CustomProperties | None = None,
    ) -> None:
        """Record an individual message within a session.

        Args:
            session_id (str): Session ID associated with the message.
            message_index (int): Message index used to sort messages in a chronological order within a session. Must be a positive integer.
            role (str): alignai.constants.ROLE_USER or alignai.constants.ROLE_ASSISTANT.
            content (str): Content of the message.
            custom_properties (dict[str, str] | None, optional): Custom properties associated with the message. Defaults to None.
        """  # noqa: E501
        validate_session_id_or_raise(session_id)
        if message_index <= 0:
            raise ValidationError("message_index must be greater than 0")
        if not content:
            raise ValidationError("content is required")
        if custom_properties:
            validate_custom_properties_or_raise(custom_properties)
        if role not in {ROLE_USER, ROLE_ASSISTANT}:
            raise ValidationError(f"Invalid message role '{role}': Message role must be either 'user' or 'assistant'")

        create_message_event = Event(
            id=uuid.uuid4().hex,
            type=EventTypes.MESSAGE_CREATE,
            create_time=datetime_to_timestamp(datetime.now(timezone.utc)),
            properties=EventProperties(
                message_properties=EventProperties.MessageProperties(
                    session_id=session_id,
                    message_index_hint=message_index,
                    message_role=(
                        EventProperties.MessageProperties.Role.ROLE_ASSISTANT
                        if role == ROLE_ASSISTANT
                        else EventProperties.MessageProperties.Role.ROLE_USER
                    ),
                    message_content=content,
                ),
                custom_properties=serialize_custom_properties(custom_properties) if custom_properties else None,
            ),
            project_id=self.project_id,
        )
        self._collect(create_message_event)

    def create_session_feedback(
        self,
        session_id: str,
        feedback_type: str,
    ):
        """Record an feedback targeting a specific session.

        Args:
            session_id (str): Session ID associated with the message.
            feedback_type (str): alignai.constants.FEEDBACK_THUMBS_UP or alignai.constants.FEEDBACK_THUMBS_DOWN.
        """  # noqa: E501
        validate_session_id_or_raise(session_id)
        if feedback_type != FEEDBACK_THUMBS_UP and feedback_type != FEEDBACK_THUMBS_DOWN:
            raise ValidationError(
                f"Invalid feedback type '{feedback_type}': Feedback type must be either 'thumbs_up' or 'thumbs_down'"
            )

        create_feedback_event = Event(
            id=uuid.uuid4().hex,
            type=EventTypes.FEEDBACK_CREATE,
            create_time=datetime_to_timestamp(datetime.now(timezone.utc)),
            properties=EventProperties(
                feedback_properties=EventProperties.FeedbackProperties(
                    session_id=session_id,
                    feedback_target=EventProperties.FeedbackProperties.TARGET_SESSION,
                    type=feedback_type,
                ),
            ),
            project_id=self.project_id,
        )
        self._collect(create_feedback_event)

    def create_message_feedback(
        self,
        session_id: str,
        message_index: int,
        feedback_type: str,
    ):
        """Record an feedback targeting a specific message.

        Args:
            session_id (str): Session ID associated with the message.
            message_index (int): Message index used to sort messages in a chronological order within a session. Must be a positive integer.
            feedback_type (str): alignai.constants.FEEDBACK_THUMBS_UP or alignai.constants.FEEDBACK_THUMBS_DOWN.
        """  # noqa: E501
        validate_session_id_or_raise(session_id)
        if message_index <= 0:
            raise ValidationError("message_index must be greater than 0")
        if feedback_type != FEEDBACK_THUMBS_UP and feedback_type != FEEDBACK_THUMBS_DOWN:
            raise ValidationError(
                f"Invalid feedback type '{feedback_type}': Feedback type must be either 'thumbs_up' or 'thumbs_down'"
            )

        create_feedback_event = Event(
            id=uuid.uuid4().hex,
            type=EventTypes.FEEDBACK_CREATE,
            create_time=datetime_to_timestamp(datetime.now(timezone.utc)),
            properties=EventProperties(
                feedback_properties=EventProperties.FeedbackProperties(
                    session_id=session_id,
                    message_index_hint=message_index,
                    feedback_target=EventProperties.FeedbackProperties.TARGET_MESSAGE,
                    type=feedback_type,
                ),
            ),
            project_id=self.project_id,
        )
        self._collect(create_feedback_event)

    def flush(self, timeout_seconds: int | None = None) -> None:
        """Dispatch all events from the buffer to Align AI.

        Args:
            timeout_seconds (int | None, optional): After the timeout, SDK will stop flushing. Defaults to 5 seconds.
        """
        if timeout_seconds is None:
            timeout_seconds = self.config.flush_timeout_seconds
        self.worker.flush(timeout_seconds)

    def close(self, timeout_seconds: int | None = None) -> None:
        """Terminate the SDK client. It will first flush all events and then shut down the SDK. It's advised to use this method for a graceful shutdown.

        Args:
            timeout_seconds (int | None, optional): After the timeout, SDK will stop flushing and the remaining data in the buffer will be lost. Defaults to 5 seconds.
        """  # noqa: E501
        if timeout_seconds is None:
            timeout_seconds = self.config.flush_timeout_seconds
        self.worker.stop(timeout_seconds)

    def _collect(self, event: Event) -> None:
        try:
            self.buffer_storage.push(event)
        except Exception as e:
            self.logger.exception(e)
