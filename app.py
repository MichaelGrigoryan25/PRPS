import random

OptionsList = ['rock', 'paper', 'scissors']
CPUOption = random.choice(ChoiceList)

UserInput = input("Choose an Option: " + OptionsList)

if UserInput == "rock" and CPUOption == "paper":
    print(CPUOption + "You Lost")
elif UserInput == "paper" and CPUOption == "scissors":
    print(CPUOption + "You Lost")
elif UserInput == "scissors" and CPUOption == "rock":
    print(CPUOption + "You Lost")
elif UserInput == CPUOption:
    print("DRAW!")
else:
    print("CPU chose: " + CPUOption + /n"You Won!")