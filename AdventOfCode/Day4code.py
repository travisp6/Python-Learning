#given a multitude of bingo cards and draw numbers, find out which card wins first
#the winning cards score is calculated by the sum of unmarked numbers on that board * the number that was just called
#the card is a 5x5 set of numbers 
#input: list of numbers from data sheet
#output: winning card's score (sum of unmarked numbers on card * the number last called)


DOES NOT WORK 1/23/22

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

#separate the boards to size 5x5
count = 0
by25 = 0
while count < 3:
    if count < 3:
        #list the boards to have placement for victory determination
        board = dict(zip(zero_twentyfive,input[by25:by25+25]))
        appended_board.append(board)
        count += 1
        by25 += 25

game_won = False
#check if a board has won
def winner():
    #check if 0-4, 5-9, 10-14, 15-19, 20-24 wins
    #check if 0,5,10,15,20 or 1,6,11,16,21 or 2,7,12,17,22 or 3,8,13,18,23 or 4,9,14,19,24 wins
    if 
        game_won = True


#start drawing cards
while game_won == False:
    for i in range(0, len(appended_board)):
        #draw the first number from draw_number list
        for j in len(i):
            if i[j] == draw_number[0]:
                #go through each board and if the number drawn is in the board change that board number to 'x'
                j[i] = 'x'
                draw_number.pop()
            #if a board has won sum the remaining numbers and multiply by last number
            winner()

