import string
from typing import Dict
from pm4py import PetriNet

from process_mining_core.datastructure.core.model.petri_net import SerializablePetriNet, create_empty_petri_net


class PetriNetWrapper:

    def __init__(self, name):
        self.net: SerializablePetriNet = create_empty_petri_net()
        self.place_before_activity: Dict[string, string] = dict()
        self.place_after_activity: Dict[string, string] = dict()
        self.concurrent_place_before_activity: Dict[string, string] = dict()
        self.concurrent_place_after_activity: Dict[string, string] = dict()
        self.concurrent_transition_before_activity: Dict[string, string] = dict()
        self.concurrent_transition_after_activity: Dict[string, string] = dict()

        self.activities: Dict[string, tuple[PetriNet.Place, PetriNet.Transition]] = dict()
        self.activities_concurrent: Dict[string, PetriNet.Transition] = dict()

    def add_start_activity(self, start_activity):
        self.net.add_start_activity(start_activity)

    def add_end_activity(self, end_activity):
        self.net.add_end_activity(end_activity)

    def add_transition_for_activity(self, activity):
        self.net.transitions.add(activity)

    def add_relation(self, predecessor, successor):
        if successor in self.place_before_activity:
            successor_place = self.place_before_activity[successor]
        else:
            successor_place = f"place_{successor}"
            self.net.add_place(successor_place)
            self.net.add_arc_place_transition(successor_place, successor)
            self.place_before_activity[successor] = successor_place

        self.net.add_arc_transition_place(predecessor, successor_place)
        self.place_after_activity[predecessor] = successor_place

    def add_concurrent_split(self, predecessor, successor):
        if predecessor in self.concurrent_place_after_activity:
            split_place = self.concurrent_place_after_activity[predecessor]
        else:
            split_place = f"place_split_{predecessor}"
            self.net.add_place(split_place)

        if predecessor in self.concurrent_transition_after_activity:
            split_transition = self.concurrent_transition_after_activity[predecessor]
        else:
            split_transition = f"split_{predecessor}"
            self.net.add_silent_transition(split_transition)
            self.net.add_arc_place_transition(split_place, split_transition)

        self.net.add_arc_transition_place(predecessor, split_place)

        if successor in self.concurrent_place_before_activity:
            successor_place = self.concurrent_place_before_activity[successor]
        else:
            successor_place = f"place_concurrent_before_{successor}"
            self.net.add_place(successor_place)
            self.net.add_arc_place_transition(successor_place, successor)

        self.net.add_arc_transition_place(split_transition, successor_place)

    def add_concurrent_join(self, predecessor, successor):
        if successor in self.concurrent_place_before_activity:
            join_place = self.concurrent_place_before_activity[successor]
        else:
            join_place = f"place_join_{successor}"
            self.net.add_place(join_place)

        if successor in self.concurrent_transition_before_activity:
            join_transition = self.concurrent_transition_before_activity[predecessor]
        else:
            join_transition = f"join_{successor}"
            self.net.add_silent_transition(join_transition)
            self.net.add_arc_transition_place(join_transition, join_place)

        self.net.add_arc_place_transition(join_place, successor)

        if predecessor in self.concurrent_place_after_activity:
            predecessor_place = self.concurrent_place_after_activity[successor]
        else:
            predecessor_place = f"place_concurrent_after_{predecessor}"
            self.net.add_place(predecessor_place)
            self.net.add_arc_transition_place(predecessor, predecessor_place)

        self.net.add_arc_place_transition(predecessor_place, join_transition)



