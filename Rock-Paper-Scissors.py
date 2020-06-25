import random
import time

choices = ["s", "r", "p"]

def game_tie():
    if answer == "s" and pc_awnswer == "s":
        print("[LOSE] pc chose rock")
    
    if answer == "r" and pc_awnswer == "r":
        print("[LOSE] pc chose rock")
    
    if answer == "p" and pc_awnswer == "p":
        print("[LOSE] pc chose rock")

def game_win():
    if answer == "r" and pc_awnswer == "s":
            print("[WIN] pc chose scissors")

    if answer == "s" and pc_awnswer == "p":
        print("[WIN] pc chose paper")

    if answer == "p" and pc_awnswer == "r":
        print("[WIN] pc chose rock")

    if answer == "p" and pc_awnswer == "s":
        print("[LOSE] pc chose scissors")

    if answer == "r" and pc_awnswer == "p":
        print("[LOSE] pc chose paper")

    if answer == "s" and pc_awnswer == "r":
        print("[LOSE] pc chose rock")

def game():
    global answer, pc_awnswer, play_again
    answer = input("what move do you want to go with (s = scissors/r = roack/p = paper): ")
    answer.lower()
    
    pc_awnswer = random.choice(choices)

# r < s, s < p, p < r

    game_win()
    game_tie()

    play_again = input("do you want to play again? ")
    play_again.lower()

game()

if play_again == "yes":
    game()

