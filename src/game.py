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

def get_winner(board: list[str]) -> str | None:
    # A player ins if any one winning line has three identical symbols and is not empty
    for a, b, c in WIN_LINES: 
        if board[a] != " " and board[a] == board[b] == board[c]: # Prevents a false win, with line of " "
            return board[a] # Return the winning symbol ("X" or "O")
    return None

def is_draw(board: list[str]) -> bool: 
    return " " not in board and get_winner(board) is None
