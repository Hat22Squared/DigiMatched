import fighters.fighter as fighter
import cards.card as card
from typing import Dict, Tuple
from fighters.fighter import Fighter
import cards.card_library as cl
from deck import Deck
import random

deck = Deck()
while deck.size() < 9:
    chosen_cards = []
    rarity_chooser = random.random()
    rare2_threshold = 0.8
    rare3_threshold = 0.98
    if rarity_chooser < rare2_threshold:
        toAddCard = random.choice(cl.tier1Cards) # choose random rarity 1 card to add
        while toAddCard in chosen_cards:
            toAddCard = random.choice(cl.tier1Cards) # choose random rarity 1 card to add
    elif rarity_chooser < rare3_threshold:
        toAddCard = random.choice(cl.tier2Cards) # choose random rarity 2 card to add
        while toAddCard in chosen_cards:
            toAddCard = random.choice(cl.tier2Cards) # choose random rarity 2 card to add
    else: 
        toAddCard = random.choice(cl.tier3Cards) # choose random rarity 2 card to add
        while toAddCard in chosen_cards:
            toAddCard = random.choice(cl.tier3Cards) # choose random rarity 2 card to add
    chosen_cards.append(toAddCard)

    tier2Add = 1 # sets tier of the card
    rarity2Add = 1 # sets the rarity of the cards to add
    for i in range(1,4): # adds 3 instances of each card
       deck.add_card(toAddCard(tier=tier2Add, instance=i, quantity=3))