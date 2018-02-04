from card_converter import card_converter
from shouldBet import shouldBet

class Player:
    VERSION = "Version_04_fix_bugs"

    def betRequest(self, game_state):
        my_player_index = game_state['in_action']
        my_player = game_state['players'][my_player_index]
        return self.get_bet_v1(my_player)

    def showdown(self, game_state):
        pass

    def get_bet_v1(my_player):
        my_stack = my_player['stack']

        my_cards = my_player['hole_cards']
        convertedCards = card_converter(my_cards)

        isBetting = shouldBet(convertedCards)
        if not isBetting :
            return 0
        return my_stack