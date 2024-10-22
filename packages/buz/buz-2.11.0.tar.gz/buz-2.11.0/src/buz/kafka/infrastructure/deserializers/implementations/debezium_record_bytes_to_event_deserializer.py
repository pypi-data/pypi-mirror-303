from __future__ import annotations

from typing import TypeVar, Type, cast, Generic

import orjson

from buz.event import Event
from buz.kafka.infrastructure.deserializers.bytes_to_message_deserializer import BytesToMessageDeserializer

T = TypeVar("T", bound=Event)


class DebeziumRecordBytesToEventDeserializer(BytesToMessageDeserializer[Event], Generic[T]):
    __STRING_ENCODING = "utf-8"

    def __init__(self, event_class: Type[T]) -> None:
        self.__event_class = event_class

    def deserialize(self, debezium_record: bytes) -> Event:
        outbox_record: dict = self.__get_outbox_record_as_dict(debezium_record)
        event_payload: dict = orjson.loads(outbox_record["payload"])

        return cast(
            T,
            self.__event_class.restore(
                id=outbox_record["event_id"], created_at=outbox_record["created_at"], **event_payload
            ),
        )

    def __get_outbox_record_as_dict(self, debezium_record: bytes) -> dict:
        decoded_string = debezium_record.decode(self.__STRING_ENCODING)
        debezium_record_json: dict = orjson.loads(decoded_string)
        return debezium_record_json["payload"]
