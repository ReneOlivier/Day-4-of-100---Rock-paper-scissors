# Day 4 of 100 - Rock, Paper, Scissors

import random

# `arts` contains the ASCII art representations for rock, paper, scissors
# in the same order as the `names` list below (index 0 -> rock, 1 -> paper,
# 2 -> scissors). These are printed to show the player's and computer's picks.
arts = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

names = ['rock', 'paper', 'scissors']

print("Let's play a classic game of Rock, Paper, Scissors!")
print("Type rock, paper, or scissors to play")

# Read the player's choice and normalize to lowercase for simple matching
player_choice = input("What do you choose? ").lower()

# Map the player's textual choice to an index in `names` (0/1/2).
# If the input isn't valid, `player_idx` will be `None` and we can abort.
player_idx = names.index(player_choice) if player_choice in names else None

# Validate input: if the player enters something unexpected, show an error
if player_idx is None:
    print("Invalid choice!")
else:
    # Choose the computer's move as a random index 0..2
    computer_idx = random.randint(0, 2)

    # Show ASCII art for both player and computer choices
    print(arts[player_idx])
    print(f"Computer chose {names[computer_idx]}")
    print(arts[computer_idx])

    # Determine the winner:
    # - If indices are equal it's a draw.
    # - Otherwise, use modular arithmetic: if (player - computer) % 3 == 1
    #   then the player's choice wins (this encodes the rock->scissors->paper
    #   cyclical relationship). For example:
    #     rock(0) beats scissors(2) -> (0 - 2) % 3 == 1
    #     paper(1) beats rock(0)     -> (1 - 0) % 3 == 1
    #     scissors(2) beats paper(1) -> (2 - 1) % 3 == 1
    if player_idx == computer_idx:
        result = "It's a draw!"
    elif (player_idx - computer_idx) % 3 == 1:
        result = "You win!"
    else:
        result = "You lose!"

    print(result)
