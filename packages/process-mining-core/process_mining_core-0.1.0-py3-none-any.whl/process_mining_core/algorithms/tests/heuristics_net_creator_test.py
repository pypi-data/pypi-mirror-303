import unittest

from process_mining_core.algorithms.stream_heuristics.heuristics_net_creator import HeuristicsNetCreator
from process_mining_core.datastructure.core.model.directly_follows_graph import DirectlyFollowsGraph
from process_mining_core.datastructure.core.model.heuristics_net import HeuristicsNet

heuristicsNetCreator: HeuristicsNetCreator = HeuristicsNetCreator(0.5, 0.8)


class HeuristicsNetCreatorTest(unittest.TestCase):

    def test_all_activities(self):
        counted_relations = dict()
        counted_relations[("b", "d")] = 3
        counted_relations[("c", "d")] = 3
        counted_relations[("b", "c")] = 3
        counted_relations[("c", "b")] = 3

        directly_follows_graph = DirectlyFollowsGraph(
            counted_relations=counted_relations,
            start_activities=[],
            end_activities=[]
        )

        heuristics_result: HeuristicsNet = heuristicsNetCreator.create_heuristics_net(directly_follows_graph)

        self.assertEqual(heuristics_result.start_activities, [])
        self.assertEqual(heuristics_result.end_activities, [])

        self.assertIn("a", heuristics_result.all_activities)
        self.assertIn("b", heuristics_result.all_activities)
        self.assertIn("c", heuristics_result.all_activities)
        self.assertEqual(3, len(heuristics_result.all_activities))

        self.assertIn(("a", "b"), heuristics_result.relations)
        self.assertIn(("a", "c"), heuristics_result.relations)
        self.assertEqual(2, len(heuristics_result.relations))

        self.assertIn(("c", "b"), heuristics_result.concurrent_activities)
        self.assertIn(("b", "c"), heuristics_result.concurrent_activities)
        self.assertEqual(2, len(heuristics_result.concurrent_activities))


