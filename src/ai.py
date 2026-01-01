from game import get_winner

AI_PLAYER = "O"
HUMAN_PLAYER = "X"

def terminal_score(board: list[str]) -> int | None: 
    """
    Return a score from the AI's perspective: 
    +1 if the AI wins, 
    -1 if the human wins, 
    0 if it's a draw, 
    None if the game is not over.
    """

    w = get_winner(board)

    if w == AI_PLAYER: 
        return 1
    if w == HUMAN_PLAYER:
        return -1
    if " " not in board: 
        return 0

    return None


def legal_moves(board: list[str]) -> list[int]:
    """Return a list of indices for legal moves on the board."""
    return [i for i in range(9) if board[i] == " "]

def minimax(board: list[str], player: str) -> int: 
    """
    Return the best achievable score from this position, asuming perfect play 
    from both sides. 
    `player` is whose turn is next: "O" (AI) or "X" (human).
    """
    score = terminal_score(board)
    if score is not None: 
        return score 
    
    moves = legal_moves(board)

    if player == AI_PLAYER:
        best_score = -2 # Worse than the worst case
        for i in moves: 
            board[i] = AI_PLAYER # Try this move
            score = minimax(board, HUMAN_PLAYER)
            board[i] = " " # Undo move

            if score > best_score: 
                best_score = score
        return best_score
    else: # HUMAN_PLAYER "X" tries to minimise the AI's score
        best_score = 2
        for i in moves: 
            board[i] = HUMAN_PLAYER
            score = minimax(board, AI_PLAYER)
            board[i] = " "

            if score < best_score: 
                best_score = score
        return best_score
         
def best_ai_move(board: list[str]) -> int: 
    """Return the index of the best move for the AI player."""
    moves = legal_moves(board)

    # Pick the move with the highest minimax score. 
    best_score = -2
    best_index = moves[0]

    for i in moves: 
        board[i] = AI_PLAYER                  # Try this move
        score = minimax(board, HUMAN_PLAYER)  # Evaluate it
        board[i] = " "                        # Undo move

        if score > best_score: 
            best_score = score
            best_index = i 
    return best_index