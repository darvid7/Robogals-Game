__author__ = 'David'

# import libraries ---------------------------------------------------------------


import tkinter

from program import computer_select
from program import battle

gameState = False

def restart():
    print("\n-----GAME RESTART-----")
    global gameState
    gameState = False
    #play_againButton.pack_forget()

    gameButton.config(text="Start")

    playerPhoto.config(image=player_hand)
    compPhoto.config(image=comp_hand)
    winnerLabel.config(text="")
    winP1Label.config(text="")
    winP2Label.config(text="")

# note need declaration to modify global var
# don't need to read

def gameControl():
    '''
    program start --> False
    game start --> True
    game end (currently True) --> do stuff and set back to False
    '''
    global gameState

    if gameState is False:
        # start
        checkInput()
    elif gameState == "Finished":
        # game either in progress or has finished
        # gameControl will only be called if finished
        # reset
        restart()

    if playerEntry.get() == "-none-":
        invalidInput()
    elif gameState == "Error":
    # gameState is Error
    # valid input
    # change to False so game can run

        gameState =False
        invalid_inputLabel.config(text="")
        checkInput()

def invalidInput():
    invalid_inputLabel.config(text="Error: Invalid input, select either scissors, paper or rock\n from the drop down "
                                   "menu")
    global gameState
    gameState = "Error"





def checkInput():
    # always valid input, except first invalid input
    print("----game processing----")
    playerName = playerNameInput.get()
    '''
    playerLabel.pack_forget()
    playerNameInput.pack_forget()
    inputLabel.pack_forget()
    options.pack_forget()
    startButton.pack_forget()
    '''

    global gameState
    if gameState is False:
        #startButton.pack_forget()
        gameState = "In progress"

        playerInput = playerEntry.get()
        if playerInput == "Scissors":
            player_move = 1

        elif playerInput == "Paper":
            player_move = 2

        elif playerInput == "Rock":
            player_move = 3

        else:
            print("Something went wrong")

            return
        if player_move > 0:
            # input valid, start battle
            battleMotion(player_move, playerName)




def battleMotion(player_move, playerName):
    print("----motion animation started----")

    playerPhoto.after(400, change1)
    playerPhoto.after(800, change2)
    playerPhoto.after(1200, change3)
    playerPhoto.after(1600, change4, player_move, playerName)



def change1():
    playerPhoto.config(image=playerMotion_a)
    compPhoto.config(image=compMotion_a)
    print('----motion image 1----')


def change2():
    playerPhoto.config(image=player_hand)
    compPhoto.config(image=comp_hand)
    print('----motion image 2----')


def change3():
    playerPhoto.config(image=playerMotion_c)
    compPhoto.config(image=compMotion_c)
    print('----motion image 3----')


def change4(player_move, playerName):
    playerPhoto.config(image=player_hand)
    compPhoto.config(image=comp_hand)
    print('----motion image 4----')

    playerPhoto.after(100,main,player_move,playerName)

    gameButton.config(text="Play again")






def main(player_move, playerName):
    print("----main process----")

    myDictionary = { 1: "Scissors",
                     2: "Paper",
                     3: "Rock"}

    computer_move = computer_select()
    # motion


    result = battle(player_move, computer_move)
    # final images


    # modify player photo
    if player_move == 1:
        playerPhoto.config(image=player_scissors)
    elif player_move == 2:
        playerPhoto.config(image=player_paper)
    elif player_move == 3:
        playerPhoto.config(image=player_rock)
    # modify computer photo
    if computer_move == 1:
        compPhoto.config(image=comp_scissors)
    elif computer_move == 2:
        compPhoto.config(image=comp_paper)
    elif computer_move == 3:
        compPhoto.config(image=comp_rock)


    winP1Label.config(text=str(playerName)+" chose " + str(myDictionary.get(player_move)), fg="black")
    winP2Label.config(text="the_Computer chose " + str(myDictionary.get(computer_move)), fg ="black")

    if result == "Draw":
        winText = result
    elif result == 1:
        winText = str(playerName) + " won !"
    else:
        winText = " the_Computer won ! "

    winnerLabel.config(text=winText, fg="red")

    global gameState
    gameState = "Finished"
    print("----finished----")

def endProgram():
    window.quit()
# -- Create GUI ------------------------------------------------------
window = tkinter.Tk()
window.title("Scissors, paper, rock!")
window.geometry("1000x1000")

# store images
player_hand = tkinter.PhotoImage(file="Image_library/player_hand.gif")

player_rock = tkinter.PhotoImage(file="Image_library/player_rock.gif")
player_paper = tkinter.PhotoImage(file="Image_library/player_paper.gif")
player_scissors = tkinter.PhotoImage(file="Image_library/player_scissors.gif")
    
playerMotion_a = tkinter.PhotoImage(file="Image_library/player_hand1.1.gif")
playerMotion_c = tkinter.PhotoImage(file="Image_library/player_hand1.2.gif")

comp_hand= tkinter.PhotoImage(file="Image_library/comp_hand.gif")

comp_rock = tkinter.PhotoImage(file="Image_library/comp_rock.gif")
comp_paper = tkinter.PhotoImage(file="Image_library/comp_paper.gif")
comp_scissors = tkinter.PhotoImage(file="Image_library/comp_scissors.gif")

compMotion_a = tkinter.PhotoImage(file="Image_library/comp_hand1.1.gif")
compMotion_c = tkinter.PhotoImage(file="Image_library/comp_hand1.2.gif")


# player name label
introLabel  = tkinter.Label(window, text="Greetings human, you have challenged a computer to a game of: \n"
                                         "Scissors,Paper, Rock\n",font=('Helvetica', 22))
#playerLabel.pack(padx=0, pady=0, side=tkinter.LEFT )
introLabel.pack()



# player name label
playerLabel  = tkinter.Label(window, text="Enter your name",font=('Helvetica', 22))
#playerLabel.pack(padx=0, pady=0, side=tkinter.LEFT )
playerLabel.pack()

# enter name of player
playerNameInput = tkinter.Entry(window)
#playerName.pack(padx=0, pady=0, side=tkinter.RIGHT)
playerNameInput.pack()

playerNameInput.delete(0, tkinter.END)
playerNameInput.insert(0, "new001")
# playerName.get() to get name input

# select label
inputLabel  = tkinter.Label(window, text="Select either scissors, paper or rock", font=('Helvetica', 22))
inputLabel.pack()

# drop down menu
playerEntry = tkinter.StringVar(window)
playerEntry.set("-none-")
options = tkinter.OptionMenu(window, playerEntry, "Scissors", "Paper", "Rock")
options.pack()

# game control button

gameButton = tkinter.Button(window, text="Start", command=gameControl ,font=('Helvetica', 22))
gameButton.pack()

invalid_inputLabel = tkinter.Label(window, text="", fg = "red", font=('Helvetica', 22))
invalid_inputLabel.pack()

# note: apparently mac dosn't like button colour changing
quitButton = tkinter.Button(window, text="Quit", bg="red",font=("Halvetica",22), command=endProgram)
quitButton.pack(side=tkinter.LEFT, anchor=tkinter.S)

tempText = ""

winP1Label = tkinter.Label(window, text=tempText,font=('Helvetica', 22), fg="white")
winP1Label.pack(side=tkinter.BOTTOM, anchor=tkinter.S)

winP2Label = tkinter.Label(window, text=tempText,font=('Helvetica', 22), fg="white")
winP2Label.pack(side=tkinter.BOTTOM, anchor=tkinter.S)

winnerLabel = tkinter.Label(window, text=tempText,font=('Helvetica', 22), fg="white")
winnerLabel.pack(side=tkinter.BOTTOM, anchor=tkinter.S)


# player hand image
playerPhoto = tkinter.Label(window, image=player_hand)
playerPhoto.pack(padx=0, pady=10, side=tkinter.LEFT, anchor=tkinter.CENTER)

# computer hand image
compPhoto = tkinter.Label(window, image=comp_hand)
compPhoto.pack(padx=0, pady=10, side=tkinter.RIGHT, anchor=tkinter.CENTER)


window.mainloop()

# note adjust size for computer/screen/os for aesthetics