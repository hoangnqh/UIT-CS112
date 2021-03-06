
def check(board, word):
    visited = [[False for j in range(len(board[0]))] for i in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if backTrack(board, word, 0, i, j, visited):
                return True

    return False

def backTrack(board, word, cur, i, j, visited):
    if cur == len(word):
        return True

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or\
            visited[i][j] or board[i][j] != word[cur]:
        return False

    visited[i][j] = True
    result = backTrack(board, word, cur + 1, i + 1, j, visited) or\
                backTrack(board, word, cur + 1, i - 1, j, visited) or\
                backTrack(board, word, cur + 1, i, j + 1, visited) or\
                backTrack(board, word, cur + 1, i, j - 1, visited)
    visited[i][j] = False

    return result

board = input()[3:-3].split("\'], [\'")
board = [a.split("\', \'") for a in board]
word = input()

if check(board, word) == True:
    print("true")
else:
    print("false")