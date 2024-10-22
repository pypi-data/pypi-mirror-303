# kafka script to generate the report

import json
import time
import logging

from typing import Optional
from typing import Dict

from jmxquery import JMXQuery
from jmxquery import JMXConnection

from neso_utils.assessment_report.kafka.metrics import KafkaMetrics
from neso_utils.assessment_report.utils.dict import aggregator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AssessmentReport:
    """
    Class to generate the report with kafka metrics and or custom metrics (e.g. metrics around
    the type of messages vehiculated).

    Most of the default metrics are around:
    - Producer latency;
    - Consumer latency;
    - Number of messages vehiculated.

    However, the user can add custom metrics to the report.

    Args:
        target_topic (str): topic to which the messages are produced
        source_topic (str, optional): topic from which the messages are consumed
        broker (str): broker to connect to
        frequency (int): how often the metrics are determined
        metrics (Dict): custom metrics to add to the report
        agg_results (bool): whether to aggregate the results or not
        export_file (bool): whether to export the report in the form of a json file or not
    """

    def __init__(
        self,
        target_topic: str,
        source_topic: Optional[str] = None,
        # TODO. adjust this value to the EKS value - but it needs to be JMX hostname and port
        broker: str = "kafka-0.kafka.default.svc.cluster.local:9101",
        frequency: int = 10,
        metrics: Dict = KafkaMetrics().to_dict(),
        agg_results: bool = False,
        export_file: bool = False,
    ):
        self.broker = broker
        self.frequency = frequency
        self.target_topic = target_topic
        self.source_topic = source_topic
        self.metrics = metrics
        self.agg_results = agg_results
        self.export_file = export_file

        self._handler()

    def _handler(self):
        """
        Heart of the operations.

        This function will be used to call all the modules from the class to produce the report.

        The course of action is:
        - Setup the connection to the broker;
        - Extract the metrics from the broker;
        - [_If needed_] Aggregate the results;
        - [_If needed_] Export the report.
        """

        prev_messages_in = 0
        self.report_data = []
        self.connection = self._setup_connection()
        self.topics = [self.target_topic, self.source_topic] if self.source_topic else [self.target_topic]

        logger.info("Collecting metrics...")

        messages_query = KafkaMetrics().messages_in_per_second(self.target_topic)

        while True:
            time.sleep(self.frequency)
            messages_in = self.connection.query([JMXQuery(messages_query)])

            if prev_messages_in >= len(messages_in):
                break

            metrics = self._extract_metrics()
            self.report_data.append(metrics)

            prev_messages_in = len(messages_in)

        if self.export_file:
            self.export_report()

        else:
            return self.report_data

    def _setup_connection(self) -> JMXConnection:
        """
        Setup the connection to the broker.
        """

        return JMXConnection(f"service:jmx:rmi:///jndi/rmi://{self.broker}/jmxrmi")

    # TODO. this function probably needs to be refactored to be more dynamic
    # we will also add custom metrics around schema validation and the messages itself
    def _extract_metrics(self) -> Dict:
        """
        Extract the metrics from the broker.
        """

        output = {topic: [] for topic in self.topics}
        kafka_metrics = KafkaMetrics().to_dict()

        for topic in self.topics:
            queries_lst = [
                JMXQuery(kafka_metrics[key](self.target_topic)) for key, val in kafka_metrics.items()
            ]

            response = self.connection.query(queries_lst)
            response_converted = {key: result.value for key, result in zip(kafka_metrics.keys(), response)}

            output[topic] = response_converted

        if self.agg_results:
            response_converted = aggregator(response_converted)

        return {
            "timestamp": time.time(),
            **response_converted,
        }

    def export_report(self, file_name: str = "kafka_report.json") -> None:
        """
        Export the report.

        The report produced will be extracted in a json file.

        Args:
            file_name (str): name of the file to export the report
        """

        try:
            logger.info("Exporting the report...")
            with open(f"{file_name}", "w") as file:
                json.dump(self.report_data, file)

        except Exception as e:
            logger.error(f"Error exporting the report: {e}")
