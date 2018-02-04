from card_converter import card_converter
from shouldBet import shouldBet

class Player:
    VERSION = "Version_03_suits"

    def betRequest(self, game_state):
        my_player_index = game_state['in_action']
        my_player = game_state['players'][my_player_index]
        my_stack = my_player['stack']

        my_cards = my_player['hole_cards']
        convertedCards = card_converter(my_cards)

        isBetting = shouldBet(convertedCards)
        if not isBetting :
            return 0
        return my_stack

    def showdown(self, game_state):
        pass
