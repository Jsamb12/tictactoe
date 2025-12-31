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

def main() -> None: 
    print("Tic-Tac-Toe Game Started")
    board = new_board()
    print_board(board)

if __name__ == "__main__":
    main()