import random

OptionsList = ['rock', 'paper', 'scissors']
CPUOption = random.choice(OptionsList)
line = "_______________________"
ErrorMessage = "Error. Please start again"
UserInput = str(input("Choose an Option -- " + str(OptionsList) + ": "))

def start():
    if UserInput == "rock" and CPUOption == "paper":
        print(line)
        print(CPUOption + "\nYou Lost")
    elif UserInput == '' and OptionsList != UserInput:
        print(ErrorMessage)
    elif UserInput == "paper" and CPUOption == "scissors":
        print(line)
        print(CPUOption + "\nYou Lost")
    elif UserInput == "scissors" and CPUOption == "rock":
        print(line)
        print(CPUOption + "\nYou Lost")
    elif UserInput == CPUOption:
        print(line)
        print("DRAW!")
    else:
        print(line + "\nCPU chose: " + CPUOption)
        print("You won!")

start()