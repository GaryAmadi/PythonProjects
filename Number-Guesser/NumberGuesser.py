import random
def number_guesser():
    #Generating secret number between 10 and 40
    secret_number = random.randint(10,40)

    attempts = 0
    max_attempts = 5

    print("Welcome to the number guesser game 🔢")
    print("I'm thinking of a number between 10 and 40")

    while attempts < max_attempts:
        try:
            guess=int(input("Your guess? "))
        except ValueError:
            print("Kindly input a number value")
            continue

        attempts += 1

        if guess < secret_number:
            print("Your guess is less than the secret number")
        elif guess > secret_number:
            print("Your guess exceeds the lucky number 🙃")
        else:
            print(f"You win!You guessed it right!The secret number is {secret_number}\nCheers mate 🍻")
            break


    if attempts == max_attempts:
            print(f"Sorry you've reached the maximum number of attempts.\nThe secret number was {secret_number}")

number_guesser()
