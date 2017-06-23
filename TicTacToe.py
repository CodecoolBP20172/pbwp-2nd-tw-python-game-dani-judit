import random
print("Welcome on board! This is a TicTacToe game designed by Kovács Judit & Koperecz Dániel.\n Have a good game!")
print("Player 1 will be 'X' and the Computer be 'O'.")
print("The left side top corner is the 1th place, and the right side bottom corner is the 9th.")
print("You can mark the fields with numbers between 1 and 9!")
name = input("Give me your name Player 1: ")


while (True):
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 1

    win = 1
    draw = -1
    running = 0

    mark = 'X'

    game = running

    def compmove():
        global lista
        lista = []
        for i in range(len(board)):
            if i == 0:
                continue
            if board[i] == ' ':
                lista.append(i)
                global computer
                computer = random.choice(lista)

    def drawboard():
        print(board[1] + "  |" + board[2] + "  |" + board[3])
        print("___|___|___")
        print(board[4] + "  |" + board[5] + "  |" + board[6])
        print("___|___|___")
        print(board[7] + "  |" + board[8] + "  |" + board[9])
        print("   |   |   ")

    def checkWin():
        global game
        if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
            game = win
        elif(board[4] == board[5] and board[6] == board[4] and board[4] != ' '):
            game = win
        elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
            game = win
        elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
            game = win
        elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
            game = win
        elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
            game = win
        elif(board[1] == board[5] and board[5] == board[9] and board[1] != ' '):
            game = win
        elif(board[7] == board[5] and board[5] == board[3] and board[7] != ' '):
            game = win
        elif(board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
            game = draw
        else:
            game = running


    while (game == running):
        print()
        drawboard()
        if(player % 2 != 0):
            print("It's your turn " + name + ' !')
            mark = 'X'
            while True:
                Choice = input("Choose a number between 1-9 to mark somewhere: ")
                try:
                    Choice = int(Choice)
                    break
                except (ValueError):
                    print("Please enter a number between 1-9: ")
            if board[Choice] == ' ':
                board[Choice] = mark
                player += 1
                checkWin()
            else:
                print("That place is already taken, please choose another!")
        else:
            compmove()
            mark = 'O'
            board[computer] = mark
            player += 1
            checkWin()

        if(game == draw):
            drawboard()
            print("Game Draw")
        elif(game == win):
            drawboard()
            player -= 1
            if(player % 2 != 0):
                print(name + " won!")
            else:
                print(name + " lost!")

            playAgain = input("Would you like to play again? Press y if yes: ")
            if playAgain != 'y':
                quit()
