# -------------------------------------
# Title:        DnD Characters
# Author:       Clint MacDonald
# Date:         Oct. 30, 2025
# Purpose:      To learn ONE WAY to implement arrays (lists)
# -------------------------------------

#region IMPORTS
import random;
#endregion

#region CONSTANTS and GLOBAL VARIABLES
STRENGTH = 0
DEXTERITY = 1
CONSTITUTION = 2
INTELLIGENCE = 3
WISDOM = 4
CHARISMA = 5

players = []                # string of player names
char_name = []              # character's name
char_species = []           # character's species
char_class = []             # character's occupation
char_age = []               # character's starting age
char_attributes = []        # storing the character's attributes

attributes = [0,0,0,0,0,0]  # character's attributes
# attributes are:
# Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma

#endregion

#region Initialization  (setting things up)
# PLAYER 0
players.append("unknown")
char_name.append("character name")
char_species.append("human")
char_class.append("fighter")
char_age.append(random.randint(18, 75))

attributes[STRENGTH] = random.randint(8,18)
attributes[DEXTERITY] = random.randint(8,18)
attributes[CONSTITUTION] = random.randint(8,18)
attributes[INTELLIGENCE] = random.randint(8,18)
attributes[WISDOM] = random.randint(8,18)
attributes[CHARISMA] = random.randint(8,18)

char_attributes.append(attributes)
#endregion

#region temp for demonstration
# PLAYER 1
players.append("Clint")
char_name.append("Savion")
char_species.append("Damphir")
char_class.append("Warlock")
char_age.append(523)

attributes = [0,0,0,0,0,0]
attributes[STRENGTH] = 8
attributes[DEXTERITY] = 12
attributes[CONSTITUTION] = 14
attributes[INTELLIGENCE] = 8
attributes[WISDOM] = 14
attributes[CHARISMA] = 18
char_attributes.append(attributes)

# PLAYER 2
players.append("Tony")
char_name.append("Ren")
char_species.append("Human")
char_class.append("Rogue")
char_age.append(19)

attributes = [0,0,0,0,0,0]
attributes[STRENGTH] = 8
attributes[DEXTERITY] = 18
attributes[CONSTITUTION] = 14
attributes[INTELLIGENCE] = 12
attributes[WISDOM] = 14
attributes[CHARISMA] = 10
char_attributes.append(attributes)
#endregion

#region printing out characters
for i in range(len(players)):
    print('-'*40)
    print("Player:      %s" % players[i])
    print("Character:   %s" % char_name[i])
    print("Species:     %s" % char_species[i])
    print("Class:       %s" % char_class[i])
    print("Age:         %i" % char_age[i])
    
    # attributes
    print("Attributes:")
    print("Strength:        %i" % char_attributes[i][STRENGTH] )
    print("Dexterity:       %i" % char_attributes[i][DEXTERITY] )
    print("Constitution:    %i" % char_attributes[i][CONSTITUTION] )
    print("Intelligence:    %i" % char_attributes[i][INTELLIGENCE] )
    print("Wisdom:          %i" % char_attributes[i][WISDOM] )
    print("Charisma:        %i" % char_attributes[i][CHARISMA] )
print('-'*40)
print("---  end of characters  ---")
#endregion