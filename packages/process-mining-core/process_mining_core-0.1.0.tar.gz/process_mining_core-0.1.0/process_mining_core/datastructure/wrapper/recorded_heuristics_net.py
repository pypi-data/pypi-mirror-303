from process_mining_core.datastructure.core.model.heuristics_net import HeuristicsNet


class RecordedHeuristicsNet:

    def __init__(self, heuristics_net: HeuristicsNet, ingestion_time: int):
        self.ingestion_time = ingestion_time
        self.heuristics_net: HeuristicsNet = heuristics_net
        self.processing_time = None

    def add_processing_time(self, processing_time):
        self.processing_time = processing_time

