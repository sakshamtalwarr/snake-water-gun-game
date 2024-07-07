import tkinter as tk
import random

def determine_winner(computer, you):
    if computer == you:
        return "It's a draw!"
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(you_choice):
    choices = {'s': 1, 'w': -1, 'g': 0}
    reverse_choices = {1: 'snake', -1: 'water', 0: 'gun'}

    you = choices[you_choice]
    computer = random.choice([-1, 0, 1])

    computer_choice_label.config(text=f"Computer chose {reverse_choices[computer]}")
    result_label.config(text=determine_winner(computer, you))

def on_choice_button_click(choice):
    play_game(choice)

# Initialize the main window
root = tk.Tk()
root.title("Snake Water Gun Game")

# Labels
instruction_label = tk.Label(root, text="Choose snake (s), water (w), or gun (g):")
instruction_label.pack()

computer_choice_label = tk.Label(root, text="Computer chose: ")
computer_choice_label.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Buttons for choices
snake_button = tk.Button(root, text="Snake", command=lambda: on_choice_button_click('s'))
snake_button.pack(side=tk.LEFT, padx=10)

water_button = tk.Button(root, text="Water", command=lambda: on_choice_button_click('w'))
water_button.pack(side=tk.LEFT, padx=10)

gun_button = tk.Button(root, text="Gun", command=lambda: on_choice_button_click('g'))
gun_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()
