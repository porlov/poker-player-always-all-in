def card_converter(cards):
        dictionary = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11 
        }

        converted_cards = []
        for card in cards:
            new_card_rank = dictionary.get(card['rank']) or int(card['rank'])
            converted_cards.append({"rank": new_card_rank, "suit": card['suit']})

        return converted_cards