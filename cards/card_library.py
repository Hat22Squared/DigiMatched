# Exploit, disengage, 

# List of cards is at the bottom

##### Tier 1 Cards #####

class Dash(Card):

    def __init__(self, tier, instance, quantity):
        self.gen_setup()
        self.name = "({0}) Dash {1}/{2}".format(tier, instance, quantity)
        self.type = "V"
        self.printed_value = 3
        self.value = self.printed_value
        self.card_text = "AFTER COMBAT: Move your fighter up to 3 spaces."
        self.boost = 2
        self.tier = tier
        self.instance = instance
        self.quantity = quantity

    def ac(self):
        if self.tier == 1:
            if 2 > 1:
                # move(fighter, spacecount=3)
                val = 1
        if self.tier == 2:
            if 2 > 1:
                # move(fighter, spacecount=4)
                val = 1
        if self.tier == 3:
            if 2 > 1:
                # move(fighter, spacecount=5, Through=True)
                val = 1
        

    def def_tier2(self):
        self.tier = 2
        self.name = "({0}) Dash {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 4
        self.card_text = "AFTER COMBAT: Move your fighter up to 4 spaces."
        self.boost = 3
        
    def def_tier3(self):
        self.tier = 3
        self.name = "({0}) Dash {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 5
        self.card_text = "AFTER COMBAT: Move your fighter up to 5 spaces through opposing fighters."
        self.boost = 4

class Feint(Card):

    def __init__(self, tier, instance, quantity):
        self.gen_setup()
        self.name = "({0}) Feint {1}/{2}".format(tier, instance, quantity)
        self.type = "V"
        self.printed_value = 2
        self.value = self.printed_value
        self.card_text = "IMMEDIATELY: Cancel all effects on the opposing fighter's card."
        self.boost = 1
        self.can_be_cancelled = False

    def im(self):
        #cancel_other_card()
        val = 1

    def ac(self):
        if self.tier == 3:
            # Draw 1 card.
            val=1

    def def_tier2(self):
        self.tier = 2
        self.name = "({0}) Feint {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 3
        self.card_text = "IMMEDIATELY: Cancel all effects on the opposing fighter's card."
        
    def def_tier3(self):
        self.tier = 3
        self.name = "({0}) Feint {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 4
        self.card_text = "IMMEDIATELY: Cancel all effects on the opposing fighter's card. \nAFTERCOMBAT: Draw 1 card."
        self.boost = 2

class Momentous_Shift(Card):

    def __init__(self, tier, instance, quantity):
        self.gen_setup()
        self.name = "({0}) Momentous Shift {1}/{2}".format(tier, instance, quantity)
        self.type = "V"
        self.printed_value = 3
        self.value = self.printed_value
        self.card_text = "DURING COMBAT: If your fighter started this turn on a different space, this card's value is a 5 instead"
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
        self.tier = 2
        self.name = "({0}) Momentous Shift {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 4
        self.card_text = "DURING COMBAT: If your fighter started this turn on a different space, this card's value is a 6 instead"
        
    def def_tier3(self):
        self.tier = 3
        self.name = "({0}) Momentous Shift {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 5
        self.card_text = "DURING COMBAT: If your fighter started this turn on a different space, this card's value is a 8 instead"
        self.boost = 2

class Regroup(Card):
    
    def __init__(self, tier, instance, quantity):
        self.gen_setup()
        self.name = "({0}) Regroup {1}/{2}".format(tier, instance, quantity)
        self.type = "V"
        self.printed_value = 1
        self.value = self.printed_value
        self.card_text = "AFTER COMBAT: Draw 1 card. If you won the combat, draw 2 instead."
        self.boost = 3

    def ac(self):
        if self.tier == 1:
            if 2 > 1:
                # Draw 1 / 2 cards
                val=1
        if self.tier == 2:
            if 2 > 1:
                # Draw 2 / 3 cards
                val=2
        if self.tier == 3:
            if 2 > 1:
                # Draw up to 3 cards
                val = 3

    def def_tier2(self):
        self.tier = 2
        self.name = "({0}) Regroup {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 2
        self.card_text = "AFTER COMBAT: Draw 2 cards. If you won the combat, draw 3 instead."
        self.boost = 4
        
    def def_tier3(self):
        self.tier = 3
        self.name = "({0}) Regroup {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 4
        self.card_text = "AFTER COMBAT: Draw up to 3 cards"
        self.boost = 5

class Skirmish(Card):
    
    def __init__(self, tier, instance, quantity):
        self.gen_setup()
        self.name = "({0}) Skirmish {1}/{2}".format(tier, instance, quantity)
        self.type = "V"
        self.printed_value = 4
        self.value = self.printed_value
        self.card_text = "AFTER COMBAT: If you won the combat, choose one of the fighters in the combat and move them up to 2 spaces."
        self.boost = 1

    def dc(self):
        if self.tier == 1:
            if 2 > 1:
                # move()
                val=1
        if self.tier == 2:
            if 2 > 1:
                # move()
                val=2
        if self.tier == 3:
            if 2 > 1:
                # move()
                val = 3

    def def_tier2(self):
        self.tier = 2
        self.name = "({0}) Skirmish {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 5
        self.card_text = "AFTER COMBAT: If you won the combat, choose one of the fighters in the combat and move them up to 3 spaces."
        
    def def_tier3(self):
        self.tier = 3
        self.name = "({0}) Skirmish {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 6
        self.card_text = "Move each of the fighters in the combat up to 3 spaces."
        self.boost = 2

##### Rarity 2 (Rarer) Cards #####

class Super_Feint(Card):

    def __init__(self, tier, instance, quantity):
        self.gen_setup()
        self.name = "({0}) Super Feint {1}/{2}".format(tier, instance, quantity)
        self.type = "V"
        self.printed_value = 4
        self.value = self.printed_value
        self.card_text = "IMMEDIATELY: Cancel all effects on the opposing fighter's card. \nAFTERCOMBAT: Draw 1 card."
        self.boost = 2
        self.can_be_cancelled = False
        self.rarity = 2

    def im(self):
        #cancel_other_card()
        val = 1

    def ac(self):
        if self.tier == 3:
            # Draw 1 card.
            val=1

    def def_tier2(self):
        self.tier = 2
        self.name = "({0}) Super Feint {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 5
        self.card_text = "IMMEDIATELY: Cancel all effects on the opposing fighter's card. \nAFTERCOMBAT: Draw 2 cards."
        
    def def_tier3(self):
        self.tier = 3
        self.name = "({0}) Super Feint {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 6
        self.card_text = "IMMEDIATELY: Cancel all effects on the opposing fighter's card. \nAFTERCOMBAT: Draw up to 2 cards."
        self.boost = 3

##### Rarity 3 (Rarest) Cards #####

class Ultimate_Feint(Card):

    def __init__(self, tier, instance, quantity):
        self.gen_setup()
        self.name = "({0}) Ultimate Feint {1}/{2}".format(tier, instance, quantity)
        self.type = "V"
        self.printed_value = 6
        self.value = self.printed_value
        self.card_text = "IMMEDIATELY: Cancel all effects on the opposing fighter's card. \nAFTER COMBAT: Draw 1 card. Recover 1 health."
        self.boost = 3
        self.can_be_cancelled = False
        self.rarity = 3

    def im(self):
        #cancel_other_card()
        val = 1

    def ac(self):
        if self.tier == 3:
            # Draw 1 card.
            val=1

    def def_tier2(self):
        self.tier = 2
        self.name = "({0}) Feint {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 6
        self.card_text = "IMMEDIATELY: Cancel all effects on the opposing fighter's card. \nAFTER COMBAT: Draw 2 cards. If you were the defender, recover 2 health. If you were the attacker, gain 1 action."
        
    def def_tier3(self):
        self.tier = 3
        self.name = "({0}) Feint {1}/{2}".format(self.tier, self.instance, self.quantity)
        self.printed_value = 6
        self.card_text = "IMMEDIATELY: Cancel all effects on the opposing fighter's card. \nAFTER COMBAT: Draw up to 3 cards. If you were the defender, recover 3 health. If you were the attacker, gain 2 actions."


tier1Cards = [Dash, Feint, Momentous_Shift, Regroup, Skirmish]

tier2Cards = [Super_Feint]

tier3Cards = [Ultimate_Feint]