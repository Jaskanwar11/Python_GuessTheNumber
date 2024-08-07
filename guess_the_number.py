import random

def guess():
    count = 0
    num = random.randint(0, 100)
    print("\nWelcome")
    while True:
        count += 1
        choice = int(input("Enter a number: "))
        if choice < num:
            print("Guess a higher number!")
        elif choice > num:
            print("Guess a lower number!")
        elif choice == num: 
            print("Congrats")
            print("You guessed it correctly in ", count, " tries!")
            break

guess()