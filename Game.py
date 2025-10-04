import random


guessNo = random.randint(0,100)

while True:
    num = int(input("input number:"))

    if num == guessNo:
        print(f" {guessNo}: you win")
        exit()
    elif num > guessNo:
        print("too high, go lower")
    else:
        print("too low, go higher")


