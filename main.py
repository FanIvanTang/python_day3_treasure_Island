def leep_year(this_year):

    is_4 = (this_year % 4) == 0
    is_100 = this_year % 100 == 0
    is_400 = this_year % 400 == 0

    if is_4:
        if is_100:
            if is_400:
                return True
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":

    print(
        '''
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
 _________|___________| ;`-.o`"=._; ." ` '`.".-` . "-._ /_______________|_______
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
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    # https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

    # Write your code below this line 👇

    if (
        input(
            "You'er at a corss road. Where do you want to go? Type 'left' or 'right': "
        )
        == "left"
    ):
        if (
            input(
                "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: "
            )
            == "wait"
        ):
            a = input(
                "You arrive at the island unharmed. Ther is a house with 3 doors. ONe red, one yellow and one blue. Which colour do you choose: "
            )
            if a == "blue":
                print("Eaten by beasts, Game Over.")
            elif a == "red":
                print("Burned by fire. Game Over.")
            elif a == "yellow":
                print("You found treasure, you win!")
            else:
                print("Game Over")
        else:
            print("You are killed by fish. Game Over.")

    else:
        print("You enter wrong direction and lost. Game Over.")
