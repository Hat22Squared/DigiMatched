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
        defender[0].hp = defender[0].hp - hp_loss

    defender[1].ac()
    attacker[1].ac()

# Get the player input, forcing the return of an int.
# The player will see the text entered as `player_text`
def get_int_input(self, player_text):
    notdigit = "That is not a valid input. Must give an int. Try again:"
    player_input = input(player_text)
    while player_input.isdigit() == False:
        player_input = input(notdigit)
    return int(player_input)



    



