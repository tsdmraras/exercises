num = input("Enter a number:")
guess = 0

while guess != num:
    guess = input("make a new guess: ")
    if guess == num:
        print("You guessed the number!")
        break
    
    print("Try again!")
    