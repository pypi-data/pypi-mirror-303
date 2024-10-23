from distributed_event_factory.core.event import CaseId

class Event:
    def __init__(self, timestamp, sensor_value, case_id: CaseId, sensor_name, group_id):
        self.timestamp = timestamp
        self.activity: any = sensor_value
        self.caseId: CaseId = case_id
        self.node: str = sensor_name
        self.group: str = group_id

    def get_case(self):
        return self.caseId

    def get_activity(self):
        return self.activity

    def get_timestamp(self):
        return self.timestamp

    def __str__(self):
        return str(self.__dict__)