# -------------------------------------
# Title:        Creating a quad golf round tracking system
# Author:       Clint MacDonald
# Date:         Oct. 30, 2025
# Purpose:      To design an array implementation system
# -------------------------------------

# Design the storage system to store the scores of 4 players playing a round of golf.  A round of golf consists of 18 holes.  You will want a way to track the total score for each player.

player_names = []
scores = []
holes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# holes will be stored inside scores[] for each player

player_names.append("Player 1") # index 0
player_names.append("Player 2") # index 1
player_names.append("Player 3") # index 2
player_names.append("Player 4") # index 3

holes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scores.append(holes) # index 0
holes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scores.append(holes) # index 1
holes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scores.append(holes) # index 2
holes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scores.append(holes) # index 3

scores[0][1] = 3
scores[0][0] += scores[0][1]

