class FrequencyDeltaPair:
    def __init__(self, delta: int):
        self.frequency = 1
        self.delta = delta

    def is_relevant(self, current_bucket_number) -> bool:
        return self.frequency + self.delta >= current_bucket_number

    def increment(self, current_bucket_number):
        self.frequency += 1
        self.delta = current_bucket_number

    def __str__(self):
        return f"({self.frequency}:{self.delta})"
