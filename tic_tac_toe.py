# Tic-Tac-Toe Game

# Function to print the board
def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Function to check for a win
def check_win(board, player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                    (0, 4, 8), (2, 4, 6)]  # Diagonals
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Function to check for a draw
def check_draw(board):
    return all(space != " " for space in board)

# Main function to play the game
def play_game():
    board = [" "] * 9  # Initialize the game board
    current_player = "X"  # Player X starts

    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is X and Player 2 is O.")
    
    while True:
        print_board(board)

        try:
            # Get the player's move
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
        
        # Update the board with the player's move
        board[move] = current_player

        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()

'''
How the Game Works:
Players take turns entering their move (a number from 1 to 9 corresponding to the grid positions).
The board is displayed after each move, and the current player's symbol (X or O) is placed on the grid.
The game checks for a winner after every move by examining all possible win patterns (rows, columns, and diagonals).
If there is a winner, the game ends and announces the winner. If there is no winner and the board is full, the game declares a draw.'''