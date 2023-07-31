import random
import math


class Fighter():
      
    def __init__(self, name, start_hp, hp, passive):

        self.name = name
        self.start_hp = start_hp
        self.hp = hp
        self.passive = passive
        self.hand = []

    # Default bot choosing an attack
    def choose_attack(self):
        # Gathers and sorts cards depending on type
        attack_cards = []
        versatile_cards = []
        for hand_index, c in enumerate(self.hand):
            if c.type == "A":
                attack_cards.append((c.name, hand_index))
            elif c.type == "V":
                versatile_cards.append((c.name, hand_index))

        # Plays attack cards randomly first if there are any
        num_attack_cards = len(attack_cards)
        if num_attack_cards != 0:
            card_choice = attack_cards[math.floor(random.random() * num_attack_cards)]
            choosen_card = get_card(card_choice[0])
            # self.hand.remove(card_choice[1])
            return choosen_card
        # Plays versatile cards randomly if there are any and no attack cards
        num_versatile_cards = len(versatile_cards)
        if num_versatile_cards !=0:
            card_choice = versatile_cards[math.floor(random.random() * num_versatile_cards)]
            choosen_card = get_card(card_choice[0])
            # self.hand.remove(card_choice[1])
            return choosen_card
        # Can check if cannot attack by seeing if return value == None
        return 
    
    # Default Bot choosing defense
    def choose_defense(self):
        # Gathers and sorts cards depending on type
        defense_cards = []
        versatile_cards = []
        for hand_index, c in enumerate(self.hand):
            if c.type == "D":
                defense_cards.append((c.name, hand_index))
            elif c.type == "V":
                versatile_cards.append((c.name, hand_index))

        # Plays defense cards randomly first if there are any
        num_defense_cards = len(defense_cards)
        if num_defense_cards != 0:
            card_choice = defense_cards[math.floor(random.random() * num_defense_cards)]
            choosen_card = get_card(card_choice[0])
            # self.hand.remove(card_choice[1])
            return choosen_card
        # Plays versatile cards randomly if there are any and no attack cards
        num_versatile_cards = len(versatile_cards)
        if num_versatile_cards !=0:
            card_choice = versatile_cards[math.floor(random.random() * num_versatile_cards)]
            choosen_card = get_card(card_choice[0])
            # self.hand.remove(card_choice[1])
            return choosen_card
        # Can check if cannot defend by seeing if return value == None
        return 
