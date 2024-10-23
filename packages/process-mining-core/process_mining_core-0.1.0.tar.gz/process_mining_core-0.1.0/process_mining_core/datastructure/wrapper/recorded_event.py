from process_mining_core.datastructure.core.event import Event


class RecordedEvent:

    def __init__(self, event: Event):
        self.ingestion_time = None
        self.processing_time = None
        self.event: Event

    def add_ingestion_time(self, ingestion_time):
        self.ingestion_time = ingestion_time

    def add_processing_time(self, processing_time):
        self.processing_time = processing_time

