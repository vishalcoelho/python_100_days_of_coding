prompt = 'You\'re at a cross road. Where do you want to go? Type "left" or "right" '
prompt_left = (
    'You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. '
    'Type "swim" to swim accross. '
)
prompt_left_wait = """
You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.
Which color do you chose? """
prompt_left_wait_red = "You entered a room filled with lava. Game Over."
prompt_left_wait_yellow = "You found the treasure. You Win!"
prompt_left_wait_blue = "You enter a room of beasts. Game Over."
prompt_left_swim = "You drowned. Game Over."
prompt_right = "Dead End. Game Over."
prompt_error = "Wrong Entry. Try again."


def treasure_island() -> str:
    """A choose-your-own-adventure story"""
    print(
        r'''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
          '''
    )

    result = prompt_error
    print(
        """
Welcome to treasure Island.
Your mission is to find the treasure.
          """.strip()
    )
    decision = input(prompt)
    if decision == "left":
        decision = input(prompt_left)
        if decision == "wait":
            decision = input(prompt_left_wait)
            if decision == "red":
                result = prompt_left_wait_red
            elif decision == "blue":
                result = prompt_left_wait_blue
            elif decision == "yellow":
                result = prompt_left_wait_yellow
            else:
                pass
        elif decision == "swim":
            result = prompt_left_swim
        else:
            pass
    elif decision == "right":
        result = prompt_right
    else:
        pass

    print(result)
    return result


if __name__ == "__main__":
    treasure_island()
