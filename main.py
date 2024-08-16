import time

ROW_LENGTH = 10
COL_LENGTH = 10


def main():
    board = [
        [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
        ["#", ".", "#", ".", ".", ".", ".", ".", ".", "."],
        [".", "#", "#", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
    draw_board(board)


def draw_board(board: list):
    new_board: list = [["." for _ in range(ROW_LENGTH)] for _ in range(COL_LENGTH)]
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            print(col, end="")
            test = calculate_neighbours(i, j, board)
            if test == "alive":
                new_board[i][j] = "#"

        print()

    print("\033[F" * (COL_LENGTH + 1))
    time.sleep(0.5)
    draw_board(new_board)


def calculate_neighbours(row: int, col: int, board: list) -> str:
    num_neighbors: int = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if board[(row + i) % ROW_LENGTH][(col + j) % COL_LENGTH] == "#":
                num_neighbors += 1

    if board[row][col] == "#" and num_neighbors > 0:
        num_neighbors -= 1

    next_state: str
    if num_neighbors in range(2, 4) and board[row][col] == "#":
        # Any live cell with two or three live neighbours lives on to the next generation.
        next_state = "alive"
    elif num_neighbors == 3 and board[row][col] == ".":
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        next_state = "alive"
    else:
        # Any live cell with more than three live neighbours dies, as if by overpopulation.
        # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        next_state = "dead"

    return next_state


if __name__ == "__main__":
    main()
