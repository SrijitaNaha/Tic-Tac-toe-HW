import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("300x300")
window.configure(bg="#FFA07A")  # Set background color to light salmon

# Create buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(window, text="", width=10, height=3, command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5, ipadx=5, ipady=5)
    buttons.append(button)

# Create a label to display the current player's turn
turn_label = tk.Label(window, text="Player 1 Turn", font=("Arial", 16))
turn_label.grid(row=3, column=0, columnspan=3)

# Game variables
current_player = 1
game_over = False
board = ["" for _ in range(9)]

# Function to handle button clicks
def button_click(index):
    global current_player, game_over

    if game_over or board[index] != "":
        return

    # Update the button text and board
    buttons[index].config(text="X" if current_player == 1 else "O")
    board[index] = "X" if current_player == 1 else "O"

    # Check for a winner
    if check_win():
        turn_label.config(text=f"Player {current_player} Wins!")
        game_over = True
    elif check_draw():
        turn_label.config(text="It's a Draw!")
        game_over = True
    else:
        # Switch to the next player
        current_player = 2 if current_player == 1 else 1
        turn_label.config(text=f"Player {current_player} Turn")

# Function to check for a win
def check_win():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != "":
            return True
    return False

# Function to check for a draw
def check_draw():
    return all(cell != "" for cell in board)

# Start the game loop
window.mainloop()