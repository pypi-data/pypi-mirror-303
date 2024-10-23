class DirectlyFollowsRelation:
    def __init__(self, predecessor, successor):
        self.predecessor = predecessor
        self.successor = successor

    def to_pair(self):
        return self.predecessor, self.successor

    def __eq__(self, other):
        if isinstance(other, DirectlyFollowsRelation):
            return other.successor == self.successor and other.predecessor == self.predecessor
        return False

    def __hash__(self):
        return hash(self.predecessor) + hash(self.successor)

    def __str__(self):
        return f"<{self.predecessor}, {self.successor}>"
