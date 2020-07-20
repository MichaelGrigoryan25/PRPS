import random

OptionsList = ['rock', 'paper', 'scissors']
CPUOption = random.choice(OptionsList)

line = "_______________________"
ErrorMessage = "Error. Please start again"
UserInput = input("Choose an Option: " + str(OptionsList))

def start():
    if UserInput == "rock" and CPUOption == "paper":
        print(line)
        print(CPUOption + "\nYou Lost")
    elif UserInput == "paper" and CPUOption == "scissors":
        print(line)
        print(CPUOption + "\nYou Lost")
    elif UserInput == "scissors" and CPUOption == "rock":
        print(line)
        print(CPUOption + "\nYou Lost")
    elif UserInput == CPUOption:
        print(line)
        print("DRAW!")
    elif UserInput == "":
        print(ErrorMessage)
        start()
    elif UserInput != OptionsList:
        print(ErrorMessage)
        start()
    else:
        print(line + "\nCPU chose: " + CPUOption)
        print("You won!")

start()