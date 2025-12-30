import random
import numpy as np
import matplotlib.pyplot as plt

states = []

for player_sum in range(12, 22):
    for dealer_card in range(2, 12):
        states.append((player_sum, dealer_card))
        
actions = ["Hit", "Stick"]

Epsilon = 0.5

def get_card():
    cards_choiced = [0, 0]
    for i in range(2):
        cards_choiced[i] = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    return cards_choiced
        

p_cards = get_card()
d_cards = get_card()

print(f'\nPlayer cards is: {p_cards}')
print(f'Dealer showing_card is: {d_cards[1]}')
        
        
# print(states)