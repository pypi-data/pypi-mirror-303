from typing import Dict, Any

from process_mining_core.algorithms.lossy_counting.frequency_delta_pair import FrequencyDeltaPair

class LossyCountingDictionary:
    def __init__(self):
        self.dictionary = dict()

    def insert(self, item: Any, bucket_number: int) -> None:
        if item in self.dictionary:
            self.dictionary[item].increment(bucket_number)
        else:
            self.dictionary[item] = FrequencyDeltaPair(bucket_number)

    def get_counted(self) -> Dict[Any, int]:
        items_with_count = dict()
        items = self.dictionary.copy()
        for item in items:
            items_with_count[item.to_pair()] = self.dictionary[item].frequency
        return items_with_count

    def clean_up(self, bucket_number: int) -> None:
        relevant_items = dict()
        for key in self.dictionary:
            frequency_delta_pair = self.dictionary[key]
            if frequency_delta_pair.is_relevant(bucket_number):
                relevant_items[key] = frequency_delta_pair
        self.dictionary = relevant_items
