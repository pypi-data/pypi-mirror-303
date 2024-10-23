from collections.abc import Mapping
from datetime import datetime

from google.protobuf.timestamp_pb2 import Timestamp

from alignai.proto.ingestion.v1alpha.event_pb2 import EventProperties


def datetime_to_timestamp(dt: datetime) -> Timestamp:
    timestamp = Timestamp()
    timestamp.FromDatetime(dt)
    return timestamp


CustomProperties = dict[str, str]


def serialize_custom_properties(
    custom_properties: CustomProperties,
) -> Mapping[str, EventProperties.CustomPropertyValue]:
    serialized_properties = {}

    for key, value in custom_properties.items():
        if isinstance(value, str):
            serialized_properties[key] = EventProperties.CustomPropertyValue(string_value=value)

    return serialized_properties
