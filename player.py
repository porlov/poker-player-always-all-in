from card_converter import card_converter
from shouldBet import shouldBet
from strategy import Strategy


class Player:
    VERSION = "Version_11"

    def get_player(self):
        player_index = self.game_state['in_action']
        return self.game_state['players'][player_index]

    def log_state(self):
        print 'STATE: ', self.game_state
        print 'STACK: ', self.player['stack']

    def betRequest(self, game_state):
        self.game_state = game_state
        self.player = self.get_player()
        
        self.log_state()

        strategy = Strategy(player=self.player, game_state=self.game_state)
        bet = strategy.get_bet()
        # bet = self.get_bet_v1(self.player)

        print 'BET: ', bet
        return bet

    def showdown(self, game_state):
        pass

    def get_bet_v1(self):
        my_stack = self.player['stack']
        my_cards = self.player['hole_cards']

        converted_cards = card_converter(my_cards)
        is_betting = shouldBet(converted_cards)

        if not is_betting:
            return 0
        return my_stack

