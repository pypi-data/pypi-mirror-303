import string
from typing import Set

from process_mining_core.datastructure.core.model.directly_follows_graph import DirectlyFollowsGraph
from process_mining_core.datastructure.core.model.heuristics_net import HeuristicsNet


class HeuristicsNetCreator:

    def __init__(self, dependency_threshold, and_threshold):
        self.dependency_threshold = dependency_threshold
        self.and_threshold = and_threshold

    def _get_predecessor(self, relation):
        return relation[0]

    def _get_successor(self, relation):
        return relation[1]

    def create_heuristics_net(self, directly_follows_graph: DirectlyFollowsGraph) -> HeuristicsNet:
        all_activities = []
        concurrent_activities = []
        self.relations = directly_follows_graph.relations

        relevant_relations: Set[tuple[string, string]] = set()
        for relation in self.relations:
            if self.get_dependency_measure(self._get_predecessor(relation), self._get_successor(relation)) > self.dependency_threshold:
                relevant_relations.add(relation)

        for relation1 in relevant_relations:
            predecessor_relation1 = self._get_predecessor(relation1)
            successor_relation1 = self._get_successor(relation1)

            if predecessor_relation1 not in all_activities:
                all_activities.append(predecessor_relation1)

            if not relation1[1] in all_activities:
                all_activities.append(successor_relation1)

            for relation2 in self.relations:
                predecessor_relation2 = self._get_predecessor(relation2)
                successor_relation2 = self._get_successor(relation2)

                if not relation1 == relation2:
                    if predecessor_relation1 == predecessor_relation2:
                        and_measure = self.get_and_measure(
                            predecessor_relation1,
                            successor_relation1,
                            successor_relation2
                        )
                        if and_measure > self.and_threshold:
                            concurrent_activities.append((successor_relation1, successor_relation2))

                    if successor_relation1 == successor_relation2:
                        and_measure = self.get_and_measure(
                            successor_relation1,
                            predecessor_relation1,
                            predecessor_relation2
                        )
                        if and_measure > self.and_threshold:
                            concurrent_activities.append((predecessor_relation1, predecessor_relation2))

        return HeuristicsNet(
            all_activities=all_activities,
            start_activities=list(directly_follows_graph.start_activities),
            end_activities=list(directly_follows_graph.end_activities),
            relations=list(relevant_relations),
            concurrent_activities=concurrent_activities
        )

    def get_count(self, relation: tuple[string, string]) -> int:
        if relation in self.relations:
            return self.relations[relation]
        return 0

    def get_and_measure(self, a, b, c):
        ab = self.get_count((a, b))
        ac = self.get_count((a, c))
        bc = self.get_count((b, c))
        cb = self.get_count((c, b))
        return (bc + cb) / (ab + ac + 1)

    def get_dependency_measure(self, a, b):
        ab = self.get_count((a, b))
        ba = self.get_count((b, a))
        return ab / (ab + ba + 1)