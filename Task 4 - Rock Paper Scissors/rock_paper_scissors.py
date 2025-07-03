import tkinter as tk
import random

def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result.set(f"Computer chose {computer_choice}")
    if user_choice == computer_choice:
        outcome.set("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        outcome.set("You win!")
    else:
        outcome.set("You lose!")

root = tk.Tk()
root.title("Rock-Paper-Scissors")

tk.Label(root, text="Choose one:").pack()

for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(root, text=choice, width=10, command=lambda c=choice: play(c)).pack(pady=2)

result = tk.StringVar()
outcome = tk.StringVar()
tk.Label(root, textvariable=result, font="Arial 12").pack(pady=10)
tk.Label(root, textvariable=outcome, font="Arial 14 bold").pack()

root.mainloop()

