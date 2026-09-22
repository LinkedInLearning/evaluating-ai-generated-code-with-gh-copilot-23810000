"""Command-line tic-tac-toe game for two human players."""


def display_board(board):
	for row in range(3):
		print(" | ".join(board[row * 3 : row * 3 + 3]))
		if row < 2:
			print("---------")


def winner(board):
	lines = (
		(0, 1, 2), (3, 4, 5), (6, 7, 8),
		(0, 3, 6), (1, 4, 7), (2, 5, 8),
		(0, 4, 8), (2, 4, 6),
	)
	for first, second, third in lines:
		if board[first] == board[second] == board[third] and board[first] in ("X", "O"):
			return board[first]
	return None


def play():
	board = [str(number) for number in range(1, 10)]
	player = "X"

	while True:
		display_board(board)
		choice = input(f"Player {player}, choose a square (1-9): ").strip()
		if not choice.isdigit() or not 1 <= int(choice) <= 9:
			print("Please enter a number from 1 to 9.")
			continue

		position = int(choice) - 1
		if board[position] in ("X", "O"):
			print("That square is already taken.")
			continue

		board[position] = player
		if winner(board):
			display_board(board)
			print(f"Player {player} wins!")
			return
		if all(square in ("X", "O") for square in board):
			display_board(board)
			print("It's a draw!")
			return
		player = "O" if player == "X" else "X"


if __name__ == "__main__":
	play()
