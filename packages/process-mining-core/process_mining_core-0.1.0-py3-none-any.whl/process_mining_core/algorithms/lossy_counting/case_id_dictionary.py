from typing import List

from process_mining_core.datastructure.core.directly_follows_relation import DirectlyFollowsRelation


class CaseIdDictionary:
    def __init__(self):
        self.start_activities = dict()
        self.dictionary = dict()

    def insert(self, case_id, activity) -> DirectlyFollowsRelation | None:
        if case_id not in self.dictionary:
            self.dictionary[case_id] = activity
            if activity in self.start_activities:
                self.start_activities[activity] += 1
            else:
                self.start_activities[activity] = 1
            return None

        last_activity = self.dictionary[case_id]
        relation = DirectlyFollowsRelation(last_activity, activity)
        self.dictionary[case_id] = activity
        return relation

    def get_start_activities(self, current_bucket_number) -> List[str]:
        start_activities = []
        for activity in self.start_activities:
            if self.start_activities[activity] >= current_bucket_number:
                start_activities.append(activity)
        return start_activities

    def get_end_activities(self, current_bucket_number) -> List[str]:
        end_activity_counts = dict()
        for case in self.dictionary:
            activity = self.dictionary[case]
            if activity in end_activity_counts:
                end_activity_counts[activity] += 1
            else:
                end_activity_counts[activity] = 1

        end_activities = []
        for activity in end_activity_counts:
            if end_activity_counts[activity] >= current_bucket_number:
                end_activities.append(activity)
        return end_activities
