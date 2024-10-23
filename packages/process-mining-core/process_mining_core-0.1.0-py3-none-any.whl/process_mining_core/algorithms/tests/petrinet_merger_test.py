import unittest

import pm4py

from process_mining_core.algorithms.petri_net_creator import PetriNetCreator
from process_mining_core.datastructure.converter.petrinet_merger import PetriNetMerger
from process_mining_core.datastructure.core.model.heuristics_net import HeuristicsNet
from process_mining_core.datastructure.core.model.petri_net import SerializablePetriNet


class PetriNetMergerTest(unittest.TestCase):
    def test(self):
        petriNetCreator: PetriNetCreator = PetriNetCreator()
        heuristics_result1: HeuristicsNet = HeuristicsNet(
            all_activities=["a", "b", "c", "d", "e", "f", "g", "h"],
            start_activities=["a"],
            end_activities=["h"],
            relations=[("a", "b"), ("a", "c"), ("c", "d"), ("c", "e"), ("d", "f"), ("f", "h"), ("b", "g"),
                       ("g", "h")],
            concurrent_activities=[("f", "g"), ("c", "b")]
        )

        heuristics_result2: HeuristicsNet = HeuristicsNet(
            all_activities=["a", "b", "c", "d", "e", "f", "g", "h"],
            start_activities=["a"],
            end_activities=["h"],
            relations=[("a", "b"), ("a", "c"), ("c", "d"), ("d", "f"), ("e", "f"), ("f", "h"), ("b", "g"),
                       ("g", "h")],
            concurrent_activities=[("f", "g"), ("c", "b")]
        )

        petri_net1: SerializablePetriNet = petriNetCreator.create_petri_net(heuristics_result1)
        petri_net2: SerializablePetriNet = petriNetCreator.create_petri_net(heuristics_result2)

        petri_net = PetriNetMerger().merge_petri_nets(petri_net1, petri_net2)

        pm4py_petrinet, pm4py_initial_marking, pmy4py_final_marking = petri_net.to_pm4py_petri_net()

        pm4py.view_petri_net(pm4py_petrinet, pm4py_initial_marking, pmy4py_final_marking)