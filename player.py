from card_converter import card_converter
from shouldBet import shouldBet
from strategy import Strategy


class Player:
    VERSION = "Version_08"

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

        # strategy = Strategy(player=self.player, game_state=self.game_state)
        # bet = strategy.get_bet()
        # print 'BET: ', bet

        return get_bet_v1(self.player)

    def showdown(self, game_state):
        pass

    def get_bet_v1(self, my_player):
        my_stack = my_player['stack']

        my_cards = my_player['hole_cards']
        convertedCards = card_converter(my_cards)

        isBetting = shouldBet(convertedCards)
        if not isBetting:
            return 0
        return my_stack
