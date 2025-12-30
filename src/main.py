__future__ import annotations 

from typing import List, Optional, Tuple

# Winning lines when the tictactoe board is represented using the indices 0-8
WIN_LINES: Tuple[Tuple[int, int, int], ...] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)

def print_board(board: List[str]) -> None: 
    def cell(i: int) -> str: 
        return board[i] if board[i] != "" else str(i + 1)
    
    rows = [
        f" {cell(0)} | {cell(1)} | {cell(2)} ",
        "---+---+---",
        f" {cell(3)} | {cell(4)} | {cell(5)} ",
        "---+---+---",
        f" {cell(6)} | {cell(7)} | {cell(8)} ",
    ]

def winner(board: List[str]) -> Optional[str]: 
    for a, b, c in WIN_LINES: 
        if board[a] != "" and board[a] == board[b] == board[c]: 
            return board[a]
    return None