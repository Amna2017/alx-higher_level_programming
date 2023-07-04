#!/usr/bin/python3
""" my new class """


import sys


def is_safe(board, row, col):
    """ Check if there is a queen in the same column"""
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    """ Check if there is a queen in the upper left diagonal"""
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    """ Check if there is a queen in the upper right diagonal"""
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    """ Check if there is solve a queens"""
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(board, 0, solutions)
    return solutions


def backtrack(board, row, solutions):
    """ back  if there is a queen"""
    if row == len(board):
        solutions.append([''.join(row) for row in board])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            backtrack(board, row + 1, solutions)
            board[row][col] = '.'


def print_solutions(solutions):
    """ print solution if there is a queen"""
    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)
