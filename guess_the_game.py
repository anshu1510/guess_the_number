#___create a simple number guessing game.
# The user get 10 chances to guess a number.
# If the number user guesses the number before 10 chances,
# Stop asking the number from the user,
# Say congrats and end the game.
# If the  user never guess the number,ask them 10 times and the game !!___



import random
num = 1

print("Welcome to the number guessing game."
      "We have a that need to be guessed."
      "You has a 10 chances.")
print("The secret no. is between 1 and 50.")
print("You have 10 chances")

secret_number = random.randint (1 , 50)
Attempts = 10
is_guess_correct = False

while num <= 10 :
    print(f"You have {Attempts} attempts left,")
    user_guess = int(input("Enter your guess :"))
    if user_guess == secret_number :
        print("congratulations, you guess is correct,")
        is_guess_correct = True
        break
    else :
        if user_guess < secret_number :
            higher_or_lower = "Higher"
        else:
            higher_or_lower = "Lower"
        print(f"your guess is wrong! Try {higher_or_lower} number.")

    num = num + 1
    Attempts -= 1
if is_guess_correct == False:
    print("Bad luck, you exhausted all your attempts and couldn't guess the number.")
print(f"The secret number was {secret_number}.Game Over!!")