import string
from typing import List, Set

from pm4py import PetriNet, Marking
from pm4py.objects.petri_net.utils.petri_utils import add_arc_from_to
from pm4py.objects.petri_net.utils import reduction


def create_empty_petri_net():
    return SerializablePetriNet(set(), set(), set(), set(), set(), set(), set())


class SerializablePetriNet:

    def __init__(
            self,
            places,
            transitions,
            silent_transitions,
            arc_place_transition,
            arc_transition_place,
            start_activities,
            end_activities):
        self.places: Set[string] = set(places)
        self.transitions: Set[string] = set(transitions)
        self.silent_transitions: Set[string] = set(silent_transitions)
        self.arc_place_transition: Set[tuple[string, string]] = set(arc_place_transition)
        self.arc_transition_place: Set[tuple[string, string]] = set(arc_transition_place)
        self.start_activities = set(start_activities)
        self.end_activities = set(end_activities)

    def add_start_activity(self, start_activity):
        self.start_activities.add(start_activity)
        start_place = f"start_{start_activity}"
        self.add_place(start_place)
        self.add_arc_place_transition(start_place, start_activity)
        
    def add_end_activity(self, end_activity):
        self.end_activities.add(end_activity)
        end_place = f"end_{end_activity}"
        self.add_place(end_place)
        self.add_arc_transition_place(end_activity, end_place)
    
    def add_place(self, place):
        self.places.add(place)

    def add_transition(self, transition):
        self.transitions.add(transition)

    def add_silent_transition(self, transition):
        self.silent_transitions.add(transition)

    def add_arc_place_transition(self, place, transition):
        self.arc_place_transition.add((place, transition))

    def add_arc_transition_place(self, transition, place):
        self.arc_transition_place.add((transition, place))

    def _get_transition(self, petri_net, name):
        for transition in petri_net.transitions:
            if transition.name == name:
                return transition

    def _get_place(self, petri_net, name):
        for place in petri_net.places:
            if place.name == name:
                return place

    def to_pm4py_petri_net(self) -> (PetriNet, Marking, Marking):
        petri_net = PetriNet()
        initial_marking = Marking()
        final_marking = Marking()

        for place in self.places:
            petri_net.places.add(PetriNet.Place(place))

        for transition in self.transitions:
            petri_net.transitions.add(PetriNet.Transition(transition, label=transition))

        for transition in self.silent_transitions:
            petri_net.transitions.add(PetriNet.Transition(transition, label=None))

        for arc in self.arc_place_transition:
            place = self._get_place(petri_net, name=arc[0])
            transition = self._get_transition(petri_net, name=arc[1])
            if place and transition:
                add_arc_from_to(place, transition, petri_net)

        for arc in self.arc_transition_place:
            transition = self._get_transition(petri_net, name=arc[0])
            place = self._get_place(petri_net, name=arc[1])
            if place and transition:
                add_arc_from_to(transition, place, petri_net)

        for start_activity in self.start_activities:
            place = self._get_place(petri_net, f"start_{start_activity}")
            initial_marking[place] = 1

        for end_activity in self.end_activities:
            place = self._get_place(petri_net, f"end_{end_activity}")
            final_marking[place] = 1

        reduced_petrinet = reduction.apply_simple_reduction(petri_net)
        return reduced_petrinet, initial_marking, final_marking
