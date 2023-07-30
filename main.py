import fighters.fighter as fighter
import cards.card as card
from typing import Dict, Tuple
from fighters.fighter import Fighter
from cards.card import Card

# hero = Hero()
# villain = Medusa()


def match(fighter1, fighter2):
    
    fighter1.hp = fighter1.starting_hp
    fighter2.hp = fighter2.starting_hp

    while fighter1.hp > 0 and fighter2.hp > 0: 
        
        f1_card = fighter1.deck.draw()
        f2_card = fighter2.deck.draw()

        combat(attacker=(fighter1,f1_card), defender=(fighter2,f2_card))



def combat(attacker: Tuple=None, defender: Tuple=None): # (Fighter, Card)

    defender[1].im()
    attacker[1].im()

    defender[1].dc()
    attacker[1].dc()

    hp_loss = attacker[1].value - defender[1].value
    if hp_loss > 0:
        defender.hp = defender.hp - hp_loss

    defender[1].ac()
    attacker[1].ac()


