import random
secret_number = random.randint(1,11)
print("***GUESS GAME***")
print("guessing the secret number from 1 to 10\nyou have 'three chance'")
i = 0
while i<3:
    guess = int(input(f"Guess {i+1}:"))
    if(guess == secret_number):
        print(f"you won! You guessed the secret number {secret_number}")
        break
    i+=1
else:
    print(f"you failed! the secret number is {secret_number}")