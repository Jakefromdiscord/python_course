import random

hello = input("Hello, what is your name?:\n")
response = hello + "," + " I'm thinking of a number between 1 and 100. Try to guess my number.\n"
print(response)

number = random.randint(1,100)

run = True
while run:
    guess = int(input("Enter your guess:"))
    if guess > number:
        print("Too high, guess agian")
    elif guess < number:
        print("Too low, guess agian")
    else:
        print("Congradulations!")
        run = False

