import tkinter as tk
from tkinter import messagebox # Import messagebox for dialog boxes

# Function to check if any player has won
def check_winner():
    global winner
    # List of all possible winning combinations (rows, columns, diagonals)
    for combo in [[0,1,2], [3,4,5], [6,7,8],   
                  [0,3,6], [1,4,7], [2,5,8],  
                  [0,4,8], [2,4,6]]:            
        # Check if all three buttons in the combo have the same non-empty text
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            # Highlight the winning buttons in light green
            buttons[combo[0]].config(bg="lightgreen")
            buttons[combo[1]].config(bg="lightgreen")
            buttons[combo[2]].config(bg="lightgreen")
            winner = True
            # Show a pop-up message announcing the winner
            messagebox.showinfo("Game Over", f"Player {buttons[combo[0]]['text']} wins!")
            return

# Function to handle button clicks
def button_click(index):
    global current_player
    # Only allow clicking if the button is empty and no winner yet
    if buttons[index]['text'] == "" and not winner:
        # Set the button text to the current player's symbol ("x" or "o")
        buttons[index]['text'] = current_player
        # Check if this move caused a win
        check_winner()
        # Switch to the other player's turn if no winner
        if not winner:
            toggle_player()

# Function to toggle the current player
def toggle_player():
     global current_player
     # Switch between "x" and "o"
     current_player = "x" if current_player == "o" else "o"
     # Update the label to show whose turn it is
     label.config(text=f"Player {current_player}'s turn")

# Function to reset the game
def reset_game():
    global current_player, winner
    current_player = "x"
    winner = False
    label.config(text=f"Player {current_player}'s turn")
    # Reset all buttons to empty text and default background
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create 9 buttons for the 3x3 Tic Tac Toe grid
buttons = [tk.Button(root, text="", font=('normal', 25), width=5, height=2,
                     command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons on the window in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

# Set the initial player to "x" and winner flag to False
current_player = "x"
winner = False

# Label to show whose turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 15))
label.grid(row=3, column=0, columnspan=3)

# Add a Reset button below the turn label
reset_button = tk.Button(root, text="Reset", font=('normal', 15), width=10, command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()
