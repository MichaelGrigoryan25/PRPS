import random

OptionsList = ['rock', 'paper', 'scissors']
CPUOption = random.choice(OptionsList)
line = "_______________________"

UserInput = input("Choose an Option: " + str(OptionsList))

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
else:
    print(line + "\nCPU chose: " + CPUOption)
    print("You won!")
