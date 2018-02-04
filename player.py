from card_converter import card_converter
from shouldBet import shouldBet
from strategy import Strategy
from post_flop import getPostFlopBet
from pre_flop import getPreFlopBet


class Player:
    VERSION = "Version_13"

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

        cardsOnFlop = game_state['community_cards']        
        isPostFlop = len(cardsOnFlop) > 0
        
        if not isPostFlop:
            strategy = Strategy(player=self.player, game_state=self.game_state)
            bet = strategy.get_bet()
            if bet > 0:
                return bet
            probability = strategy.player_hand.get_probability()
            return getPreFlopBet(probability, self.game_state, self.player)
            

        # post flop
        if isPostFlop: 
            return getPostFlopBet(game_state, self.player)
        
        return bet
            
        # bet = self.get_bet_v1(self.player)
        print 'BET: ', bet

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

