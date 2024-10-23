import datetime
from typing import List

import pandas
from pandas import DataFrame

from process_mining_core.datastructure.core.event import Event


class SerializableEventLog:
    def __init__(self, events: List[Event]):
        self.events = events

    def to_pm4py_event_log(self):
        event_log = dict()
        event_log["concept:name"] = {}
        event_log["time:timestamp"] = {}
        event_log["case:concept:name"] = {}
        event_log["date"] = {}

        for i, event in enumerate(self.events):
            event_log["concept:name"][i] = event.sensor_value
            event_log["time:timestamp"][i] = pandas.to_datetime(event.timestamp)
            event_log["case:concept:name"][i] = event.case_id
            event_log["date"][i] = pandas.to_datetime(datetime.datetime.now())

        return DataFrame(data=event_log)
