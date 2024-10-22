# script reserved to the kafka metrics definition

from typing import Dict
from typing import Callable

from dataclasses import dataclass

@dataclass
class KafkaMetrics:
    """
    Class to generate the default kafka metrics at the topic level
    """

    def messages_in_per_second(self, topic: str) -> str:
        return f"kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec,topic={topic}"

    def messages_lag(self, topic: str) -> str:
        return (
            f"kafka.consumer:type=consumer-fetch-manager-metrics,client-id=*,topic={topic},partition=*"
        )

    def messages_out_per_second(self, topic: str) -> str:
        return f"kafka.server:type=BrokerTopicMetrics,name=MessagesOutPerSec,topic={topic}"

    def bytes_in_per_second(self, topic: str) -> str:
        return f"kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec,topic={topic}"

    def bytes_out_per_second(self, topic: str) -> str:
        return f"kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec,topic={topic}"

    def fetch_latency_avg(self, topic: str) -> str:
        return f"kafka.server:type=BrokerTopicMetrics,name=FetchLatencyAvg,topic={topic}"

    def produce_latency_avg(self, topic: str) -> str:
        return f"kafka.server:type=BrokerTopicMetrics,name=ProduceLatencyAvg,topic={topic}"

    def consumer_latency_avg(self, topic: str) -> str:
        return f"kafka.server:type=BrokerTopicMetrics,name=ConsumerLatencyAvg,topic={topic}"

    def number_of_partitions(self, topic: str) -> str:
        return f"kafka.server:type=Topic,name={topic},*"

    def to_dict(self) -> Dict[str, Callable]:
        """
        Convert the KafkaMetrics to a dictionary.
        """

        return {
            "messages_in_per_second": self.messages_in_per_second,
            "messages_out_per_second": self.messages_out_per_second,
            "bytes_in_per_second": self.bytes_in_per_second,
            "bytes_out_per_second": self.bytes_out_per_second,
            "fetch_latency_avg": self.fetch_latency_avg,
            "produce_latency_avg": self.produce_latency_avg,
            "consumer_latency_avg": self.consumer_latency_avg,
            "number_of_partitions": self.number_of_partitions,
        }
