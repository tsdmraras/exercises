import random
import time

number = int(input("Enter a number between 1-100: "))  
guess = 0

start_time = time.time()  

while guess != number:
    guess = random.randint(1, 100)
    print("Guessing: ", guess)
    if guess == number:
        print("You guessed the number!")
        break

end_time = time.time()  

elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time, "seconds")
