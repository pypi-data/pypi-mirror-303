from abc import abstractmethod, ABC
from typing import List
from buz.event.subscriber import Subscriber


class KafkaConsumeStrategy(ABC):
    @abstractmethod
    def get_topics(self, subscriber: Subscriber) -> List[str]:
        pass

    @abstractmethod
    def get_subscription_group(self, subscriber: Subscriber) -> str:
        pass
