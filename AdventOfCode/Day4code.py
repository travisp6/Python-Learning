#given a multitude of bingo cards and draw numbers, find out which card wins first
#the winning cards score is calculated by the sum of unmarked numbers on that board * the number that was just called
#the card is a 5x5 set of numbers 
#input: list of numbers from data sheet
#output: winning card's score (sum of unmarked numbers on card * the number last called)


with open('dataforAdventCode.txt', "r") as file:
    input = [x for x in file.read().split()]
#create the list of numbers that will be called
draw_number = [37,60,87,13,34,72,45,49,61,27,97,88,50,30,76,40,63,9,38,67,82,6,59,90,
99,54,11,66,98,23,64,14,18,4,10,89,46,32,19,5,1,53,25,96,2,12,86,58,41,68,95,8,7,3,85,
70,35,55,77,44,36,51,15,52,56,57,91,16,71,92,84,17,33,29,47,75,80,39,83,74,73,65,78,69,
21,42,31,93,22,62,24,48,81,0,26,43,20,28,94,79]
zero_twentyfive = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

#create the boards
appended_board = []
def bingo_boards(numbers):
    #separate the boards to size 5x5
    count = 0
    by25 = 0
    while count < 3:
        if count < 3:
            #dictionary the boards to have placement for victory determination
            board = dict(zip(zero_twentyfive,input[by25:by25+25]))
            appended_board.append(board)
            count += 1
            by25 += 25
        print(board)

game_won = False
#check if a board has won
def winner(victory):
    #check if 0-4, 5-9, 10-14, 15-19, 20-24 wins
    #check if 0,5,10,15,20 or 1,6,11,16,21 or 2,7,12,17,22 or 3,8,13,18,23 or 4,9,14,19,24 wins
    if appended_board[0] == 'x' and appended_board[1] == 'x' and appended_board[2] == 'x' and appended_board[3] == 'x' and appended_board[4] == 'x' or \
    appended_board[5] == 'x' and appended_board[6] == 'x' and appended_board[7] == 'x' and appended_board[8] == 'x' and appended_board[9] == 'x' or \
    appended_board[10] == 'x' and appended_board[11] == 'x' and appended_board[12] == 'x' and appended_board[13] == 'x' and appended_board[14] == 'x' or \
    appended_board[15] == 'x' and appended_board[16] == 'x' and appended_board[17] == 'x' and appended_board[18] == 'x' and appended_board[19] == 'x' or \
    appended_board[20] == 'x' and appended_board[21] == 'x' and appended_board[22] == 'x' and appended_board[23] == 'x' and appended_board[24] == 'x' or \
    appended_board[0] == 'x' and appended_board[5] == 'x' and appended_board[10] == 'x' and appended_board[15] == 'x' and appended_board[20] == 'x' or \
    appended_board[1] == 'x' and appended_board[6] == 'x' and appended_board[11] == 'x' and appended_board[16] == 'x' and appended_board[21] == 'x' or \
    appended_board[2] == 'x' and appended_board[7] == 'x' and appended_board[12] == 'x' and appended_board[17] == 'x' and appended_board[22] == 'x' or \
    appended_board[3] == 'x' and appended_board[8] == 'x' and appended_board[13] == 'x' and appended_board[18] == 'x' and appended_board[23] == 'x' or \
    appended_board[4] == 'x' and appended_board[9] == 'x' and appended_board[14] == 'x' and appended_board[19] == 'x' and appended_board[24] == 'x':
        game_won = True

        
#play the game
def playing(runit):
    #call first number[i] in list
    
    #if a board has won sum the remaining numbers in dictionary and multiply by last number

    pass

print(bingo_boards(input))
#board = dict(zip(zero_twentyfive,input[:25]))
#board2 = dict(zip(zero_twentyfive,input[25:50]))
#print(board)
#print(board2)
#full_boards = [board,board2]
#print(full_boards)
#print(bingo_board(input))