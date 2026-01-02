## Tic Tac Toe Game using Python Tkinter

## Project Overview
This project is a simple graphical Tic Tac Toe game built using Python and the Tkinter library.  
It allows two players to play alternately on the same system with a clean and interactive user interface.

The game automatically detects winning combinations and highlights the winning cells.  
A reset option is provided to start a new game without restarting the application.

## Features
Two player gameplay using X and O  
Interactive graphical interface using Tkinter  
Automatic win detection with popup notification  
Winning cells highlighted visually  
Reset button to restart the game  
Turn indicator showing the active player  

## Technologies Used
Python  
Tkinter GUI library  

## How the Game Works
The game creates a 3x3 grid using Tkinter buttons.  
Each button represents a cell on the board.  
Players take turns clicking on empty cells.  
After every move the game checks for a winning condition.  
If a player wins a message box is displayed and the winning cells are highlighted.

## Game Logic
Winning combinations include rows columns and diagonals  
Button clicks are disabled once a winner is detected  
Global state is used to track current player and game status  

## Project Structure
main.py contains the complete game logic and UI code  

## How to Run the Project
Make sure Python is installed on your system  
Clone or download this repository  
Open a terminal in the project folder  
Run the following command

