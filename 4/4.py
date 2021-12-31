boards = []


class Board:
    def __init__(self):
        self.board = [[] for _ in range(5)]
        self.complete = False
        self.score = False
        self.rowsComplete = [0 for _ in range(5)]
        self.colsComplete = [0 for _ in range(5)]

    def mark(self, num):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == num:
                    self.board[i][j] = None
                    self.rowsComplete[i] += 1
                    self.colsComplete[j] += 1
                    if self.rowsComplete[i] == 5 or self.colsComplete[j] == 5:
                        self.complete = True
                        self.score = self._score(num)
                        return True
        return False

    def _score(self, mark):
        total = 0
        for i in range(5):
            for j in range(5):
                if self.board[i][j] != None:
                    total += self.board[i][j]

        return total*mark


with open('./4/input') as f:
    random_nums = list(map(int, f.readline().split(',')))
    while True:
        single_board = Board()
        line = 0
        if f.readline() == "":
            break
        for i in range(5):
            for num in f.readline().split():
                single_board.board[line].append(int(num))
            line += 1
        boards.append(single_board)


def find_winning_board():
    for num in random_nums:
        for b in boards:
            if b.complete:
                continue
            won_p = b.mark(num)
            if won_p:
                last_won_board = b
    return last_won_board


winning_board = find_winning_board()

print(winning_board.score)
