import random

secret_number = 0
difficulty = 1


def generate_number():
    global secret_number
    secret_number = random.randint(1, difficulty)
    return


def get_guess_from_user():
    try:
        num = int(input(f"please enter a number between 1 and {difficulty}"))
        if num < 1 or num > difficulty:
            print(f"please enter a number between 1 and {difficulty}")
        else:
            return num

    except ValueError:
        print("please enter a number")


def compare_results():
    if secret_number == get_guess_from_user():
        return True
    else:
        return False


def play(dif):
    global difficulty
    difficulty = dif
    generate_number()
    return compare_results()
