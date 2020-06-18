#!/usr/bin/env python3

import sys

class HausregelError(Exception):
    pass

class Sudoku:

    def __init__(self, raw_board, id):
        self.board = [[0 for x in range(9)] for x in range(9)] 
        for i in range(9):
            for j in range(9):
                self.board[i][j] = raw_board[i][j]
        self.id = id
        self.verbose = False

    def print_board(self):
        print(f"Board {self.id}:")
        for i, r in enumerate(self.board):
            for j, c in enumerate(r):
                
                sys.stdout.write(f"{c if c != '0' else '.'} ")
                if j%3 == 2 and j != 8:
                    sys.stdout.write("| ")
            print()
            if i%3 == 2 and i != 8:
                print(3*"-------")

    def get_candidates_for_field(self, r, c):
        """
        We assume this field is 0, so not determined yet
        """
        candidates = [str(i) for i in list(range(1,10))]
        for n in self.numbers_by_row(r):
            try:
                candidates.remove(n)
            except:
                pass
        for n in self.numbers_by_column(c):
            try:
                candidates.remove(n)
            except:
                pass        
        for n in self.numbers_by_block(r, c):
            try:
                candidates.remove(n)
            except:
                pass        
        return candidates

    def numbers_by_row(self, r):
        numbers = [] 
        for i in range(9):
            number = self.board[r][i]
            if number != '0':
                numbers.append(number)
        return numbers

    def numbers_by_column(self, c):
        numbers = [] 
        for i in range(9):
            number = self.board[i][c]
            if number != '0':
                numbers.append(number)
        return numbers

    def numbers_by_block(self, r, c):
        big_r = (r//3) * 3
        big_c = (c//3) * 3
        numbers = []
        for i in range(big_r, big_r+3):
            for j in range(big_c, big_c+3):
                number = self.board[i][j]
                if number != '0':
                    numbers.append(number)
        return numbers

    def solve(self):
        while True:
            if not self.solve_next_field():
                break
        # check if there are zeros remaining on the board
        if self.check_board_for_zeros():
            print("We can not solve this sudoku yet. Have a look:")
            self.print_board()
        return

    def check_board_for_zeros(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '0':
                    return True
        return False
                    

    def solve_next_field(self):
        if self.naked_singles():
            return True
        if self.hausregel_blocks():
            return True
        if self.hausregel_rows():
            return True
        if self.hausregel_columns():
            return True
        return False

    def naked_singles(self):
        # check for naked singles (in your area)
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '0':
                    c = self.get_candidates_for_field(i,j)
                    if len(c) == 1:
                        self.board[i][j] = str(c[0])
                        return True
        return False

    def hausregel_blocks(self):
        # hausregel for blocks
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                possible_digits = [str(i) for i in list(range(1,10))]
                for n in self.numbers_by_block(i,j):
                    possible_digits.remove(n)
                candidates = {}
                for r in range(3):
                    for c in range(3):
                        pos_r = i+r
                        pos_c = j+c
                        if self.board[pos_r][pos_c] != '0':
                            continue
                        candidates[pos_r, pos_c] = self.get_candidates_for_field(pos_r, pos_c)
                if self.check_digits_against_candidates(possible_digits, candidates, "blocks"):
                    return True
        return False

    def hausregel_rows(self):
        for i in range(9):
            possible_digits = [str(i) for i in list(range(1,10))]
            for n in self.numbers_by_row(i):
                possible_digits.remove(n)    
            candidates = {}
            for j in range(9):
                if self.board[i][j] != '0':
                    continue
                candidates[i, j] = self.get_candidates_for_field(i, j)
            if self.check_digits_against_candidates(possible_digits, candidates, "rows"):
                return True
        return False

    def hausregel_columns(self):
        for j in range(9):
            possible_digits = [str(i) for i in list(range(1,10))]
            for n in self.numbers_by_column(j):
                possible_digits.remove(n)    
            candidates = {}
            for i in range(9):
                if self.board[i][j] != '0':
                    continue
                candidates[i, j] = self.get_candidates_for_field(i, j)
            if self.check_digits_against_candidates(possible_digits, candidates, "columns"):
                return True
        return False

    def check_digits_against_candidates(self, possible_digits, candidates, method="unknown"):
        for digit in possible_digits:
            try:
                last_position = None
                for k,v in candidates.items():
                    if digit in v:
                        if last_position:
                            raise HausregelError()
                        last_position = k
                if last_position:
                    if self.verbose:
                        print(f"We found a number by hausregel ({method}):")
                        print(f" we changed {self.board[last_position[0]][last_position[1]]} to {digit}")
                        print(f" at position {last_position}")
                        print(f" candidates for this block:")
                        print(candidates)
                        self.print_board()
                    self.board[last_position[0]][last_position[1]] = digit
                    if self.verbose:
                        self.print_board()
                        print()
                    return True
            except HausregelError:
                continue
        return False

    def get_solution_digits(self):
        return int(f"{self.board[0][0]}{self.board[0][1]}{self.board[0][2]}")

def load_sudoku_from_number(n):
    n_str = str(n)
    if len(n_str) == 1:
        n_str = f"0{n_str}"
    with open("sudoku.txt", "r") as f:
        raw_sudoku = f.readlines()
    sudoku = []
    iter_sudoku = iter(raw_sudoku)
    for l in iter_sudoku:
        if l.find(f"Grid {n_str}") != -1:
            for i in range(9):
                sudoku.append(next(iter_sudoku))
            return Sudoku(sudoku, n)


if __name__ == "__main__":

    if len(sys.argv) == 1:
        result = 0
        for i in range(1,51):
            s = load_sudoku_from_number(i)
            s.solve()
            result += s.get_solution_digits()
        print(result)
    else:
        s = load_sudoku_from_number(int(sys.argv[1]))
        s.verbose = True
        s.print_board()
        print()
        s.solve()
        s.print_board()
        print()
        print(s.get_solution_digits())