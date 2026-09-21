"""A small command-line tic-tac-toe game against the computer."""

import random


def print_board(board):
	"""Display the current board."""
	for row in range(3):
		print(" " + " | ".join(board[row * 3 : row * 3 + 3]))
		if row < 2:
			print("---+---+---")


def winner(board):
	"""Return the winning mark, or None when there is no winner."""
	lines = (
		(0, 1, 2), (3, 4, 5), (6, 7, 8),
		(0, 3, 6), (1, 4, 7), (2, 5, 8),
		(0, 4, 8), (2, 4, 6),
	)
	for first, second, third in lines:
		if board[first] == board[second] == board[third] != " ":
			return board[first]
	return None


def computer_move(board):
	"""Choose an available square for the computer."""
	available = [index for index, square in enumerate(board) if square == " "]
	return random.choice(available)


def play_game():
	"""Run one interactive game and return when it is over."""
	board = [" "] * 9
	player = "X"

	while True:
		print_board(board)
		if player == "X":
			choice = input("Your turn, choose a square (1-9): ").strip()
			if not choice.isdigit() or not 1 <= int(choice) <= 9:
				print("Please enter a number from 1 to 9.")
				continue

			square = int(choice) - 1
			if board[square] != " ":
				print("That square is already taken.")
				continue
		else:
			square = computer_move(board)
			print(f"Computer chooses square {square + 1}.")

		board[square] = player
		game_winner = winner(board)
		if game_winner:
			print_board(board)
			print(f"Player {game_winner} wins!")
			return
		if " " not in board:
			print_board(board)
			print("It's a draw!")
			return
		player = "O" if player == "X" else "X"


if __name__ == "__main__":
	play_game()
