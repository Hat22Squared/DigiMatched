from card import Card

class Momentous_Shift(Card):

    def __init__(self):
        self.gen_setup()
        self.name = "Momentous Shift (1)"
        self.type = "V"
        self.printed_value = 3
        self.value = self.printed_value
        self.card_text = "If your fighter started this turn on a different space, this card's value is a 5 instead"
        self.boost = 1

    def dc(self):
        if self.tier == 1:
            if 2 > 1:
                self.value = 5
        if self.tier == 2:
            if 2 > 1:
                self.value = 6
        if self.tier == 3:
            if 2 > 1:
                self.value = 8

    def def_tier2(self):
        self.name = "Momentous Shift (2)"
        self.printed_value = 4
        self.card_text = "If your fighter started this turn on a different space, this card's value is a 6 instead"
        
    def def_tier3(self):
        self.name = "Momentous Shift (3)"
        self.printed_value = 5
        self.card_text = "If your fighter started this turn on a different space, this card's value is a 8 instead"
        self.boost = 2