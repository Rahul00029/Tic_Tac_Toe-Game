
def analyseboard(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if (board[cb[i][0]] != 0 and (board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]])):
            return board[cb[i][0]]
    return 0;


def minMax(board, player):
    x = analyseboard(board)
    if x != 0:
        return x * player
    value = -2
    pos = -1
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -minMax(board, player * -1)
            board[i] = 0
            if (score > value):
                value = score
                pos = i
    if pos == -1:
        return 0
    return value


def computerTurn(board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -minMax(board, -1)
            board[i] = 0
            if (score > value):
                value = score
                pos = i

    board[pos] = 1;


def player1Turn(board):
    pos = int(input("\nChoose the position of X from [1,2,3...,9]:"))
    if board[pos - 1] != 0:
        print("\nWrong move !!!")
        player1Turn(board)
    else:
        board[pos - 1] = -1


def player2Turn(board):
    pos = int(input("\nChoose the position of O from [1,2,3...,9] :"))
    if board[pos - 1] != 0:
        print("\nWrong move !!!")
        player2Turn(board)
    else:
        board[pos - 1] = 1


def showboard(board):
    print("\nCurrent state of the board \n\n")
    for i in range(0, 9):
        if i > 0 and i % 3 == 0:
            print("\n")
        if board[i] == 0:
            print("_", end=" ")
        if board[i] == -1:
            print("X", end=" ")
        if board[i] == 1:
            print("O", end=" ")
    print("\n\n");


def main():
    choice = int(input("Enter 1 for single player 2 for multiplayer : "))
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if (choice == 1):
        print("Computer : O vs You : X ")
        player = int(input("You want to play 1(st) or 2(nd) :"))
        for i in range(0, 9):
            if (analyseboard(board) != 0):
                break
            if (i + player) % 2 == 0:
                computerTurn(board)
            else:
                showboard(board)
                player1Turn(board)

    else:
        for i in range(0, 9):
            if (analyseboard(board) != 0):
                break
            if i % 2 == 0:
                showboard(board)
                player1Turn(board)

            else:
                showboard(board)
                player2Turn(board)

    x = analyseboard(board)
    if x == 0:
        showboard(board)
        print("\nDraw!!!")
    if x == -1:
        showboard(board)
        print("\nPlayer X wins !!")
    if x == 1:
        showboard(board)
        print("\nPlayer O wins !!")

main()