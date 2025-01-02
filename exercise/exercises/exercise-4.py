number = int(input("Enter a number between 1-100: "))
min = 1
max = 100
guess = 0

while number != guess:
    guess = (min + max) // 2
    print("Guessing: ", guess)
    if guess < number:
        min = guess + 1
    elif guess > number:
        max = guess - 1
    else:
        print("I found the number!")
        break
    