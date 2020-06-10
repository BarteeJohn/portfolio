from random import randint
x = int(input("Type 1 for rock, 2 for paper, and 3 for scissors: "))
correct = randint(1, 3)
print("the computer has chosen", correct)
if correct == x:
    print("Tie")
if correct != x and x == 1 and correct == 3:
    print("You win!")
if correct > x and x != 1 and correct != 3:
    print("You lose!")
if correct < x and x != 1 and correct != 3:
    print("You win!")   