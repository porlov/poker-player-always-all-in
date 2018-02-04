from models.card import Card
from models.hand import Hand

def test(player, prob):
    card1, card2 = player
    hand = Hand(Card(**card1), Card(**card2))
    hand_prob = hand.get_probability() 
    assert hand_prob == prob 

if __name__ == '__main__':
    data = ({"suit": "hearts", "rank": "A"}, 
    { "suit": "hearts", "rank": "9"})
    prob = 44.8
    test(data, prob)
    