import random
import time
import os


def game():
    user_choice = input("Pick:...\n  # ")
    os.system("clear")
    comp_choice = random.choice(computer_terminology)
    if user_choice in rock:
        if comp_choice in rock:
            print("Draw")
        if comp_choice in papers:
            print("You lose")
        if comp_choice in siccor:
            print("You won")

    if user_choice in papers:
        if comp_choice in rock:
            print("YOu won")
        if comp_choice in papers:
            print("Drwaq")
        if comp_choice in siccor:
            print("YOu Lose")

    if user_choice in siccor:
        if comp_choice in rock:
            print("You lose")
        if comp_choice in papers:
            print("YOu won")
        if comp_choice in siccor:
            print("Draw")


rock = ["rock", "Rock", "r", "R"]
papers = ["papers", "Papers", "p", "p"]
siccor = ["siccors", "Scissors", "S", "s"]

computer_terminology = ["Rock", "Papers", "Scissors"]

print("Welcome to the rock, papers and sissors game!")
time.sleep(0.1)

while True:
    game()


