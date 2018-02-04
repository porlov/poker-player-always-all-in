from models.card import Card
from models.hand import Hand


class Strategy:
    FOLD_BET = 0

    def __init__(self, player, game_state):
        self.player = player
        self.game_state = game_state
        self.player_hand = self._get_player_hand()

    def _get_player_hand(self):
        card1, card2 = self.player['hole_cards']
        return Hand(Card(**card1), Card(**card2))

    def _get_active_players_count(self):
        count = 0

        for player in self.game_state['players']:
            if int(player['stack']) > 0:
                count = count + 1

        return count

    def _get_bound(self):
        active_players_count = self._get_active_players_count()

        if active_players_count > 3:
            return 44
        if active_players_count == 3:
            return 36
        else:
            return 40

    def all_in(self):
        return self.player['stack']

    def get_bet(self):
        if self.player_hand.get_probability() > self._get_bound():
            return self.all_in()

        return self.FOLD_BET
