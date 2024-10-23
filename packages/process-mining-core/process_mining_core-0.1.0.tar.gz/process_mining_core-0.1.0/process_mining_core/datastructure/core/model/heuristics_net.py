import string
from typing import List


class HeuristicsNet:
    def __init__(self, all_activities, start_activities, end_activities, relations, concurrent_activities):
        self.all_activities: List[string] = all_activities
        self.start_activities: List[string] = start_activities
        self.end_activities: List[string] = end_activities
        self.relations: List[tuple[string, string]] = relations
        self.concurrent_activities: List[tuple[string, string]] = concurrent_activities

    def get_successors_of(self, activity):
        successors = []
        for relation in self.relations:
            if relation[0] == activity:
                successors.append(relation[1])
        return successors

    def get_concurrent_successors_of(self, activity):
        successors_of_activities = self.get_successors_of(activity)
        concurrent_successors = []
        for concurrent in self.concurrent_activities:
            if concurrent in successors_of_activities:
                concurrent_successors.append(concurrent)
        return concurrent_successors

    def get_predecessors_of(self, activity):
        successors = []
        for relation in self.relations:
            if relation[1] == activity:
                successors.append(relation[0])
        return successors

    def get_concurrent_predecessors_of(self, activity):
        predecessors_of_activities = self.get_predecessors_of(activity)
        concurrent_predecessors = []
        for concurrent in self.concurrent_activities:
            if concurrent in predecessors_of_activities:
                concurrent_predecessors.append(concurrent)
        return concurrent_predecessors
