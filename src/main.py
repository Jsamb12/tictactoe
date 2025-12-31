#  Winning indices for Tic-Tac-Toe
WIN_LINES = [
    (0, 1, 2), 
    (3, 4, 5), 
    (6, 7, 8), 
    (0, 3, 6), 
    (1, 4, 7), 
    (2, 5, 8), 
    (0, 4, 8), 
    (2, 4, 6),
]

def new_board() -> list[str]:
    return [" "] * 9

def print_board(board: list[str]) -> None: 
    def cell(i: int) -> str: 
        # Show X / O if present, else show cell number
        return board[i] if board[i] != " " else str(i + 1)

    # Display the board
    print(f" {cell(0)} | {cell(1)} | {cell(2)} \n"
          f"---+---+---\n"
          f" {cell(3)} | {cell(4)} | {cell(5)} \n"
          f"---+---+---\n"
          f" {cell(6)} | {cell(7)} | {cell(8)} \n")

def parse_move(text: str) -> int | None: 
    text = text.strip() # Handles leading/trailing whitespace

    if not text.isdigit(): 
        return None 
    
    n = int(text) # 1..9
    if 1 <= n <= 9: 
        return n - 1 # Convert to 0-based index
    return None

def get_move(board: list[str], player: str) -> int: 
    while True: 
        raw = input(f"Player {player}, enter your move (1-9): ")
        idx = parse_move(raw)

        if idx is None: 
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if board[idx] != " ":
            print("Cell already occupied. Choose another cell.")
            continue

        return idx
    
def get_winner(board: list[str]) -> str | None:
    # A player ins if any one winning line has three identical symbols and is not empty
    for a, b, c in WIN_LINES: 
        if board[a] != " " and board[a] == board[b] == board[c]: # Prevents a false win, with line of " "
            return board[a] # Return the winning symbol ("X" or "O")
    return None

def is_draw(board: list[str]) -> bool: 
    return " " not in board and get_winner(board) is None

def main() -> None: 
    print("Tic-Tac-Toe Game Started")

    board = new_board()
    current = "X"

    while True: 
        print_board(board)

        w = get_winner(board)
        if w: 
            print(f"Player {w} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        idx = get_move(board, current)
        board[idx] = current

        current = "O" if current == "X" else "X"
        print()

if __name__ == "__main__":
    main()