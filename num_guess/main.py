from art import logo
import random
print(logo)

lowest = 1
highest = 100

level = str(input("Choose mode, Easy or Hard: ")).lower()


def easy_mode():
    print("Guess a number between 1 and 100\nYou have ten attempts")
    attempts = 10
    guess = int(input("Guess a number :"))
    number = range(lowest, highest+1)
    answer = random.choice(number)
    while attempts > 0:
        if guess == answer:
            print(f"You win! The answer was {answer}")
            break
        elif guess > answer:
            print("Too high")
            attempts -= 1
            print(f"You have {attempts} attempts remaining")
            guess = int(input("Guess again :"))
        elif guess < answer:
            print("Too low")
            attempts -= 1
            print(f"You have {attempts} attempts remaining")
            guess = int(input("Guess again :"))
    if attempts == 0:
        print(f"You lose! The answer was {answer}")
    else:
        pass


def hard_mode():
    print("Guess a number between 1 and 100\nYou have five attempts")
    attempts = 5
    guess = int(input("Guess a number "))
    number = range(lowest, highest+1)
    answer = random.choice(number)
    while attempts > 0:
        if guess == answer:
            print(f"You win✌! The answer was {answer}")
            break
        elif guess > answer:
            print("Too high")
            attempts -= 1
            print(f"You have {attempts} attempts remaining")
            guess = int(input("Guess again :"))
        elif guess < answer:
            print("Too low")
            attempts -= 1
            print(f"You have {attempts} attempts remaining")
            guess = int(input("Guess again :"))
    if attempts == 0:
        print(f"You lose! The answer was {answer}")
    else:
        pass


def main():
    if level == "easy":
        easy_mode()

    elif level == "hard":
        hard_mode()


main()
