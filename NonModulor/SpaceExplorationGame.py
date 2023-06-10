

# Space Exploration text-based game
# Description: A thriller text-based game.

# ASCII ART
print('''
*****************************
       _________
      (=========)
      |=========|
      |====_====|
      |== / \ ==|
      |= / _ \ =|
    _  |=| ( ) |=|
    /=\ |=|     |=| /=\ 
    |=| |=|     |=| |=|
    |=| |=|  _  |=| |=|
    |=| |=| | | |=| |=|
    |=| |=| | | |=| |=|
    |=| |=| | | |=| |=|
    |=| |/  | |  \| |=|
    |=|/    | |    \|=|
    |=/     |_|     \=|
    |(_______________)|
    |=| |_|__|__|_| |=|
    |=|   ( ) ( )   |=|
    /===\           /===\ 
   |||||||         |||||||
   -------         -------
    (~~~)           (~~~)
*****************************
''')


def swampBiome():
    swampBiome = input("Upon landing you are met with swamp based biome. Type 'leave' to leave planet or 'exit' to exit ship:\n").lower()

    if swampBiome == "exit":
        print(f"In order to carry your mission as the captain of the Enterprise you wear your suit of armor, arm yourself, and head out into the unknown in the name of science. As soon as you step off the ship a T-REX eats you whole. \nGame Over (You were disgested alive in the T-REX acidic stomach on planet {planetName})")
    elif swampBiome == "leave":
        print(f"While trying to leave the planet. Your ship is struck down by a large creature. You do not survive the crash. \nGame Over(You burned alive on planet {planetName})")
    else:
        print("uhhh... you are not fit to be captain since you couldn't pick out of 2 choices. Game over.")


print("Welcome to Starship Enterprise, you have arrived at a red planet; located in the deep space sector 14. Your mission is to explore the planet for living life forms and habitable zones and record valuable data.")

# Player Choices
planetName = input("You search the computer database for pre-existing data. beep, boop, beep! \nThis planet is not present in the current space charts. Since you have discovered this planet, you have the privilege to name it. Please name the planet: \n")

landing = input(f"You are cruising at a safe distance from planet {planetName}, Type 'enter' to enter or 'leave' to leave:\n").lower()
if landing == "enter":
    swampBiome()
elif landing == "leave":
    print("You left without fulfilling your mission. You were stripped of all titles and dishonorably discharged. You spent rest of your days as a lowly sell sword. \nGame Over (You are a loser)")
else:
    print("uhhh... you are not fit to be captain since you couldn't pick out of 2 choices. Game over.")
