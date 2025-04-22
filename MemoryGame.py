import random
import os
import time
import sys

difficulty = 10


def generate_sequence():
    num_list = []
    while len(num_list) < difficulty:
        num_list.append(random.randint(1, 101))
    return num_list


def get_list_form_user():
    user_list = []
    while len(user_list) < difficulty:
        user_list.append(input("enter the next number you remember"))
    return user_list


def is_list_equal(generated_list, user_list):
    if generated_list == user_list:
        return True
    else:
        return False


def play(dif):
    global difficulty
    difficulty = dif
    random_seq = generate_sequence()
    for i in random_seq:
        print(i)
        time.sleep(0.7)
        if os.name == 'nt':
            os.system('cls')

    return is_list_equal(random_seq, get_list_form_user())
