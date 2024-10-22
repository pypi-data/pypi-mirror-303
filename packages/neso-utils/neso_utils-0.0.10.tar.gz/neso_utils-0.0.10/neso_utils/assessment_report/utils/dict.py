# python utils for dictionaries

from typing import Dict
from typing import List

from collections import defaultdict

def aggregator(raw_dict: List[Dict]) -> Dict:
    """
    Instead of returning all the values of metrics for a certain key, this function
    will return the average value of all the metrics collected.

    _Example_:

    >>> input_dict = {
            'source_topic': [
                {'metric_1': 100, 'metric_2': 200},
                {'metric_1': 200, 'metric_2': 200},
                {'metric_1': 300, 'metric_2': 200},
            ],
            'target_topic': [
                {'metric_1': 100, 'metric_2': 200},
                {'metric_1': 200, 'metric_2': 200},
                {'metric_1': 300, 'metric_2': 200},
            ],
        },
    ]

    >>> _aggregate_raw_dict(input_dict)
    [
        {
            'source_topic': {'metric_1': 200, 'metric_2': 200},
            'target_topic': {'metric_1': 200, 'metric_2': 200},
        }
    ]

    Args:
        raw_dict (List[Dict]): dictionary with the raw values to be aggregated

    Returns:
        Dict: dictionary with the average values of the metrics
    """

    aggregator = defaultdict(lambda: defaultdict(list))

    for topic, metrics in raw_dict.items():
        for result in metrics:
            for key, val in result.items():
                aggregator[topic][key].append(val)

    return {
        topic: {key: sum(val) / len(val) for key, val in metrics.items()}
        for topic, metrics in aggregator.items()
    }