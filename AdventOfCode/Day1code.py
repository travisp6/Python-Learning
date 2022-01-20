#take the depth and compare it to previous depth to see if it increases or decreases and determine how many times this happens
#input: depth list
#output: number of increases
def depth_measurement(number):
    position = 0
    increase = 0
    decrease = 0
    #use a while loop to add the number of increases and decreases
    while position < len(number)-1:
        for i in range(1, len(number)):
            if number[i-1] < number[i]:
                increase += 1
                position += 1
            else:
                decrease += 1
                position += 1
    return increase

#alt + shift + i
filetoread = open('dataforAdventCode.txt', "r")
a = filetoread.read().split()
print(depth_measurement(a))