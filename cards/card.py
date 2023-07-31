

# Class to represent each individual card
class Card():

    def __init__(self):
        #placeholder
        value = 1
    
    # Default setup to set ALL parameters to default values
    # All specific cards will call and then overwrite the
    # relevant parameters to minimize card updates
    def gen_setup(self):
        # Tells which card it is
        self.name = "Title"
        # "V"-versatile, "A"-attack, "D"-defense, "S"-scheme
        self.type = "V" 
        # The net value of an attack. Can change with effect
        self.value = 2
        # The printed value of an attack card. Can only change between tiers
        self.printed_value = 2
        # A card's Boost Value
        self.boost = 1
        # Boolean for if a card can be cancelled or not
        self.can_be_cancelled = True
        # How liely it will be to have the card in your deck
        self.rarity = 1
        # Which upgrade tier the card is on. 1 is the lowest
        self.tier = 1
        # Maximum tier a card can be upgraded to
        self.max_tier = 3
        # The name and details visible to the user
        self.nameplate = "({0}) {1}".format(self.tier, self.name)
        # The effect text visible to the player
        self.card_text = "Blank Card Text"
        # Number of copies of this card in the deck
        self.num_in_deck = 1
        return
    
    # Function to trigger the card's immediately effects
    def im(self):
        if self.type == "S":
            return
        
        return
    
    # Function to trigger the card's immediately effects
    def dc(self):
        if self.type == "S":
            return
        
        return

    # Function to trigger the card's immediately effects
    def ac(self):
        if self.type == "S":
            return
        
        return
    
    # Redefines card to tier 2 parameters
    def def_tier2(self):
        return
    
    # Redefines card to tier 3 parameters
    def def_tier3(self):
        return
    
    # Redefines card to tier 3 parameters
    def def_tier4(self):
        return
    
    # Redefines card to tier 3 parameters
    def def_tier5(self):
        return

    # Returns if a card can be upgraded:
    def can_upgrade(self):
        return self.tier < self.max_tier
    
    # Upgrades the card 1 tier
    def upgrade(self):
        if self.can_upgrade():
            self.tier = self.tier + 1
            if self.tier == 2:
                self.def_tier2()
            if self.tier == 3:
                self.def_tier3()
            if self.tier == 4:
                self.def_tier4()
            if self.tier == 5:
                self.def_tier5()
        else:
            # Signals failure to upgrade
            return 0
        
    def toString(self):
        return self.nameplate
