def jose_game(what_computer, what_human):
    if what_computer == what_human:
        return "It's a tie!"
    elif (what_computer == "rock" and what_human == "scissors") or \
         (what_computer == "scissors" and what_human == "paper") or \
         (what_computer == "paper" and what_human == "rock"):
        return "You lose!"
    else:
        return "You WON!"
    

def display_result(human_choice):
    import random
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = jose_game(computer_choice, human_choice)
    label_result = tk.Label(window, text=f"Computer chose {computer_choice}. {result}")
    label_result.pack()



import tkinter as tk

window = tk.Tk()
window.title("Paper Rock Scissor Game")

label_instructions = tk.Label(window, text="Choose rock, paper, or scissors!")
label_instructions.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: display_result("rock"))
rock_button.pack()

paper_button = tk.Button(window, text="Paper", command=lambda: display_result("paper"))
paper_button.pack()

scissors_button = tk.Button(window, text="Scissors", command=lambda: display_result("scissors"))
scissors_button.pack()

tk.mainloop()