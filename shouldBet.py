def shouldBet(cards):
  firstCard = cards[0]['rank']
  secondCard = cards[1]['rank']

  if firstCard == secondCard and firstCard > 7 and secondCard > 7:
    return True

  if firstCard > 10 and secondCard > 10:
    return True
  
  return False

  # highiestRankCard = cards[0] if cards[0]['rank'] > cards[1]['rank'] else cards[1]
  # lowestRankCard = cards[1] if cards[1]['rank'] > cards[0]['rank'] else cards[0]

  # if highiestRankCard['rank'] == 14 and isSuted(highiestRankCard, lowestRankCard):
  #   return True

  # if highiestRank > 13 and isSuted(highiestRankCard, lowestRankCard):
  #   return True

  # return False

def isSuted(firstCard, secondCard):
  return firstCard['suit'] == secondCard['suit']
