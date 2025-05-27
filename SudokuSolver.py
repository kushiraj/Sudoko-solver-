class SudokuSolver:
    def __init__(self):
        self.recursive_calls = 0

    def is_valid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] == c:
                return False
            if board[row][i] == c:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                return False
        return True

    def solve_sudoku(self, board):
        self.recursive_calls += 1
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        if self.is_valid(board, i, j, str(c)):
                            board[i][j] = str(c)
                            if self.solve_sudoku(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True

    def print_board(self, board):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" ")
            print()

def main():
    board = []
    for _ in range(9):
        row = list(input().strip())
        board.append(row)
    solver = SudokuSolver()
    if solver.solve_sudoku(board):
        solver.print_board(board)
        print("Number of recursive calls:", solver.recursive_calls)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()
