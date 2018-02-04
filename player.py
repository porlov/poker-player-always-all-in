from card_converter import card_converter
class Player:
    VERSION = "Version_01"

    def betRequest(self, game_state):
        my_player_index = game_state['in_action']
        my_player = game_state['players'][my_player_index]
        my_stack = my_player['stack']

        return my_stack

    def showdown(self, game_state):
        pass


    
