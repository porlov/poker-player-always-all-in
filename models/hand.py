from models.card import Card


class Hand:
    HANDS_FILE_NAME = 'pre_flop.txt'

    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.probabilities = None

    def get_probability(self, players_amount=3):
        all_hands = self.get_all_hands(players_amount=players_amount)
        self_hand = filter(lambda x: x == self, all_hands)[0]
        probability = self_hand.probabilities[players_amount-2]

        return probability

    @classmethod
    def get_all_hands(cls, players_amount=3):
        hands = []

        for line in open(cls.HANDS_FILE_NAME):
            chunks = line.replace('%', '').replace('\n', '').split('\t')
            short_description, probabilities = chunks[0], map(float, chunks[1:])

            rank1 = short_description.replace('T', '10')[0]
            rank2 = short_description.replace('T', '10')[1]
            suited = (len(short_description) == 3 and short_description[2] == 's')
            suit1 = 'fake_suit'
            suit2 = 'fake_suit' if suited else 'fake_suit_offsuited'

            card1 = Card(rank=rank1, suit=suit1)
            card2 = Card(rank=rank2, suit=suit2)
            hand = Hand(card1, card2)
            hand.probabilities = probabilities

            hands.append(hand)

        hands = sorted(hands, key=lambda hand: hand.probabilities[players_amount-2], reverse=True)
        return hands

    @property
    def suited(self):
        return self.card1.suit == self.card2.suit

    def __eq__(self, other):
        return (
           (self.card1 == other.card1 and self.card2 == other.card2) or
           (self.card1 == other.card2 and self.card2 == other.card1)
        ) and (self.suited == other.suited)

    def __repr__(self):
        return ' '.join([str(self.card1), str(self.card2), str(self.probabilities)])
