def getPostFlopBet(game_state, current_player):
  cardsNumber = len(game_state['community_cards'])
  bet = game_state['current_buy_in'] - current_player['bet']
  stack = current_player['stack']
  minRaise = game_state['minimum_raise']

  table = {
    1: bet,
    2: bet,
    3: (1/64 * stack),
    4: (1/32 * stack),
    5: (1/16 * stack)
  }

  if game_state['bet_index'] == 0 and cardsNumber == 5:
    return minRaise

  if bet > table[cardsNumber]:
    return bet

  return 0






