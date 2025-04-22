import random

import requests

difficulty = 1


def get_money_interval(t):
    url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json"
    response = requests.get(url)
    data = response.json()
    ils_value = data["usd"]["ils"]
    interval = (t * ils_value - (5 - difficulty)), (t * ils_value + (5 - difficulty))
    return interval


def get_guess_from_user():
    try:
        guess = int(input("Enter your guess for the ILS value of the given USD amount: "))
        return guess
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def play(dif):
    global difficulty
    difficulty = dif
    rand = random.randint(1, 100)
    print(f"the USD amount is: {rand}")

    interval = get_money_interval(rand)
    print(interval)
    guess = get_guess_from_user()
    if interval[0] < guess < interval[1]:
        return True
    return False
