class ChessBoard():
    def __init__(self,size):
        self.size = size
        self.columns = []

    def nextRow(self,column):
        self.columns.append(column)

    def removeRow(self):
        return self.columns.pop()

    def isSafe(self,column):
        row = len(self.columns)

        for queen_column in self.columns:
            if column == queen_column:
                return False

        for queen_row,queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False

        for queen_row,queen_column in enumerate(self.columns):
            if ((self.size - queen_column)-queen_row == (self.size - column)-row):
                return False

        return True

    def display(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print("Q", end=" ")
                else:
                    print(".",end=" ")
            print()

def solve(size):
    board = ChessBoard(size)
    number_of_solutions = 0
    row=0
    column=0
    while True:
        while column < size:
            if board.isSafe(column):
                board.nextRow(column)
                row+=1
                column=0
                break
            else:
                column+=1
        if (column == size or row == size):
            if row == size:
                board.display()
                print()
                number_of_solutions+=1
                board.removeRow()
                row-=1
            try:
                prev_column = board.removeRow()
            except IndexError:
                break
            row -=1
            column=1+prev_column
    print(number_of_solutions)

n = int(input("enter size wanted"))

solve(n)
