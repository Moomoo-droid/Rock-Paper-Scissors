import random
import time

choices = ["s", "r", "p"]

def game_win(player_answer, opponent_answer):


def game():
    answer = input("what move do you want to go with (s = scissors/r = roack/p = paper): ")
    
    pc_awnswer = random.choice(choices)

# r < s, s < p, p < r

    if answer == "r" and pc_awnswer == "s":
        print("[WIN] pc chose scissors")
