import random
import time

choices = ["s", "r", "p"]

def game_win():
    if answer == "r" and pc_awnswer == "s":
            print("[WIN] pc chose scissors")

    if answer == "s" and pc_awnswer == "p":
        print("[WIN] pc chose paper")

    if answer == "p" and pc_awnswer == "r":
        print("[WIN] pc chose rock")

    if answer == "r" and pc_awnswer == "s":
        print("[LOSE] pc chose scissors")

    if answer == "r" and pc_awnswer == "p":
        print("[LOSE] pc chose paper")

    if answer == "s" and pc_awnswer == "r":
        print("[LOSE] pc chose rock")

def game():
    global answer, pc_awnswer
    answer = input("what move do you want to go with (s = scissors/r = roack/p = paper): ")
    
    pc_awnswer = random.choice(choices)

# r < s, s < p, p < r

    game_win()

game()
