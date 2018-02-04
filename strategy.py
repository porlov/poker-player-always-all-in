from models.card import Card
from models.hand import Hand


class Strategy:
    BOUND = 44
    FOLD_BET = 0

    def __init__(self, player, game_state):
        self.player = player
        self.game_state = game_state
        self.player_hand = self._get_player_hand()

    def _get_player_hand(self):
        card1, card2 = self.player['hole_cards']
        return Hand(Card(**card1), Card(**card2))

    def all_in(self):
        return self.player['stack']

    def get_bet(self):
        if self.player_hand.get_probability() > self.BOUND:
            return self.all_in()
        return self.FOLD_BET
