import tkinter

def gameControl():
    print("--- game start ---")
def endProgram():
    print("--- End program ---")

# -- Create GUI ------------------------------------------------------
window = tkinter.Tk()
window.title("Scissors, paper, rock!")
window.geometry("1000x1000")

# store Images
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