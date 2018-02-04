def getPreFlopBet(probability, game_state, player):
  current_by_in = game_state.current_buy_in
  ourBet = player.bet
  if probability > 30 and current_by_in < 120:
    return current_by_in - ourBet
  return 0