######################################################################################
#
#             Creates a deck of Card objects for a fighter to draw from
#
######################################################################################

from cards.card import Card

class Deck():

    def __init__(self):
        self.size = 0
        self.contents = []

    def add_card(self, card:Card):
        self.contents.append(card)
        self.size += 1

    # Upgrades all copies of a card in the deck
    # Returns the number of cards upgraded
    def upgrade_all_copies(self, card_name):
        num_cards_upgraded = 0
        for c in self.contents:
            if c.name == card_name:
                c.upgrade()
                num_cards_upgraded += 1
        return num_cards_upgraded
            

    # returns the unique names of cards in the deck
    def get_card_names(self):
        names = []
        for c in self.contents:
            if c.name not in names:
                names.append(c.name)
        return names
        
    
    def toString(self):
        result = "Deck Contents: {\n"
        for index, card in enumerate(self.contents):
            result += "Card #{} ".format(index+1) + card.toString() + "\n"
        result += "}"
        return result
            

