"""
@author: David Lei
@since: 22/03/2016
@modified: 

"""
__author__ = 'David'

import random

def menu():
    print("\n")
    print("Moves")
    print("1.Scissors")
    print("2.Paper")
    print("3.Rock")

def computer_select():
    move = random.randint(1,3)
    return move

def main():

    user_name = str(input("Enter your name: "))
    computer_name = "the_Computer"

    run = True
    while run:
        try:
            menu()
            # only accepts integers
            user_move = int(input("Chose an item: "))
            print("\n")
            if user_move == 1 or user_move == 2 or user_move== 3:

                computer_move = computer_select()
                result = battle(user_move, computer_move)

                process_winner(user_move, user_name, result, computer_move, computer_name)

                print("\n")
                again = str(input("Press any key to play again, type n then press enter to quit: "))

                if again.upper() == "N":
                    run = False
            else:
                print("Error: Invalid integer")
        except ValueError:
            print("Error: Integer not entered")

def process_winner(user_move, user_name, result, computer_move, computer_name):
    myDictionary = { 1: "Scissors",
                     2: "Paper",
                     3: "Rock"}

    p1move = myDictionary.get(user_move)
    p2move = myDictionary.get(computer_move)
    print(str(user_name) + " chose " + str(p1move))
    print(str(computer_name) + " chose " + str(p2move))
    if result == "Draw":
        print(result)
    elif result == 1:
        print(str(user_name) + " won !")
    else:
        print(str(computer_name) + " won !")




def battle(p1move, p2move):
    '''
    1.Scissors
    2.Paper
    3.Rock

    :param p1move:
    :param p2move:
    :return: 'Draw' for a draw, 1 for player 1 wins, 2 for player 2 wins
    '''
    if p1move == p2move:            # all draws, lower module can use sic = sic rock = ock etc
        result = "Draw"
    elif p1move == 1 and p2move == 2:   # scissors > paper
        result = 1
    elif p1move == 1 and p2move == 3:   # scissors < rock
        result = 2
    elif p1move == 2 and p2move == 1:   # paper < scissors
        result = 2
    elif p1move == 2 and p2move == 3:   # paper > rock
        result = 1
    elif p1move == 3 and p2move == 1:   # rock > scissors
        result = 1
    elif p1move == 3 and p2move == 2:   # rock < paper
        result = 2
    else:
        print("Something went wrong")
        result = 0
    return result



if __name__ == "__main__":
    main()

