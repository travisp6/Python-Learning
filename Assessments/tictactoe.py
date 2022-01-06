#Create Tic Tac Toe

board = [0,1,2,3,4,5,6,7,8,9]

#the board function/print
def the_board():
    print(board[1],board[2],board[3])
    print(board[4],board[5],board[6])
    print(board[7],board[8],board[9])
    print()

#put choice on board function
def choice_on_board(choice):
    pick_a_number = int(input("Pick a number 1 to 9: "))
    board[pick_a_number] = "o"
    the_board()

def choice_on_board2(choice):
    pick_a_number = int(input("Pick a number 1 to 9: "))
    board[pick_a_number] = "x"
    the_board()    

#if you won function
def winner():
    if board[1] == 'x' and board[2] == 'x' and board[3] == 'x' or \
    board[4] == 'x' and board[5] == 'x' and board[6] == 'x' or \
    board[7] == 'x' and board[8] == 'x' and board[9] == 'x' or \
    board[1] == 'x' and board[4] == 'x' and board[7] == 'x' or \
    board[1] == 'x' and board[5] == 'x' and board[9] == 'x' or \
    board[3] == 'x' and board[6] == 'x' and board[9] == 'x' or \
    board[2] == 'x' and board[5] == 'x' and board[8] == 'x' or \
    board[3] == 'x' and board[5] == 'x' and board[7] == 'x' or \
    board[1] == 'o' and board[2] == 'o' and board[3] == 'o' or \
    board[4] == 'o' and board[5] == 'o' and board[6] == 'o' or \
    board[7] == 'o' and board[8] == 'o' and board[9] == 'o' or \
    board[1] == 'o' and board[4] == 'o' and board[7] == 'o' or \
    board[1] == 'o' and board[5] == 'o' and board[9] == 'o' or \
    board[3] == 'o' and board[6] == 'o' and board[9] == 'o' or \
    board[2] == 'o' and board[5] == 'o' and board[8] == 'o' or \
    board[3] == 'o' and board[5] == 'o' and board[7] == 'o':
        print("Winner!!")
        play = 0
        return winner(True)
    else:
        return False


#run the game with while loop

play = 1
while play == True:
    winner()
    choice_on_board(board)
    winner()
    choice_on_board2(board)
