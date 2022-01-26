#consider horizontal and vertical lines, where x1 = x2 or y1 = y2, 
#determine if there are overlapping lines and count how many points
#input x1,y1 -> x2,y2
#example 
#    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
#    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
#output the number of points that overlap

#create a list of data points
#from the data points create a list of covered data points
#create a grid
#put the covered data points on the grid
#count the number of data points that overlap

with open('dataforAdventCode.txt', "r") as file:
    input = [x for x in file.read().split()]

x1 = int(input[0])
x2 = int(input[2])
y1 = int(input[1])
y2 = int(input[3])

list1 = [0]*1000*1000

def checking(number):
    x1 = int(input[0])
    x2 = int(input[2])
    y1 = int(input[1])
    y2 = int(input[3])
    if int(input[1]) == int(input[3]):
        #when x1 is < x2 set xone to abs(x1-x2)
        if (int(input[0]) - int(input[2])) < 0:
            xone = abs(int(input[0]) - int(input[2]))+1
            #add all points to list1
            for j in range(0, xone):
                list1[y1*(10)+x1+j] += 1
            del input[0:4]
        elif (int(input[0]) - int(input[2])) > 0:
            xone = abs(int(input[2]) - int(input[0]))+1
            for j in range(0, xone):
                list1[y1*(10)+x1-j] += 1
            del input[0:4]
        else:
            del input[0:4]
    elif int(input[0]) == int(input[2]):
        #when y1 is < y2 set xone to abs(y1-y2)
        if (int(input[1]) - int(input[3])) < 0:
            xone = abs(int(input[1]) - int(input[3]))+1
            #add all points to list1
            for j in range(0, xone):
                list1[x1+(10*(j+1))] += 1
            del input[0:4]
        elif (int(input[1]) - int(input[3])) > 0:
            xone = abs(int(input[3]) - int(input[1]))+1
            for j in range(0, xone):
                list1[x1+(10*(j+1))] += 1
            del input[0:4]
        else:
            del input[0:4]
    else:
        del input[0:4]
for ii in range(500):
    checking(input)

count = 0
for i in list1:
    if i > 1:
        count = count + 1
print('part 1 count: ', count)