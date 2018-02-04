class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return self.rank == other.rank

    def __repr__(self):
        return '<{}, {}>'.format(self.rank, self.suit)
