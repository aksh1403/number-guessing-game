import random

target = random.randint(1,100)
guess = int(input("enter your guess : "))
count = 1

while guess!=target :
    if guess<target :
        print("too low")
    elif guess>target :
        print("too high")
    count = count + 1
    guess = int(input("enter new guess : "))
print("\n\n")
print("correct. you got it right in", count, "attempts")