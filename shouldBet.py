def shouldBet(cards):
  firstCard = cards[0]['rank']
  secondCard = cards[1]['rank']

  if(firstCard == secondCard and firstCard > 7 and secondCard > 7) {
    return True
  }

  if(firstCard > 10 and secondCard > 10) {
    return True
  }