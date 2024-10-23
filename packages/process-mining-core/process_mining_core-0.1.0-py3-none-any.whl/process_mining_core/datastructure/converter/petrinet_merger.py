import copy

from process_mining_core.datastructure.core.model.petri_net import SerializablePetriNet

class PetriNetMerger:

    def merge_petri_nets(self, net1: SerializablePetriNet, net2: SerializablePetriNet):
        petri_net1 = copy.deepcopy(net1)
        petri_net2 = copy.deepcopy(net2)

        for start_activity in petri_net1.start_activities:
            petri_net2.add_start_activity(start_activity)

        for end_activity in petri_net1.end_activities:
            petri_net2.add_end_activity(end_activity)

        for transition in petri_net1.transitions:
            petri_net2.add_transition(transition)

        for place in petri_net1.places:
            petri_net2.add_place(place)

        for arc in petri_net1.arc_place_transition:
            petri_net2.add_arc_place_transition(arc[0], arc[1])

        for arc in petri_net1.arc_transition_place:
            petri_net2.add_arc_transition_place(arc[0], arc[1])

        return petri_net2
