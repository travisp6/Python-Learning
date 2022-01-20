#Take the horizontal position, depth, and aim input to check where your sub is at
#down increases aim by x, up decreases aim by x, forward increases horizontal position by x and increases depth by aim * x
#input: up/down/forward
#output: horizontal position * depth

def position_depth(number):
    #create horizontal position and depth counter and aim
    horizontal_position = 0
    depth = 0
    aim = 0
    #check if keyword is forward, down, or up
    for i in number:
        #split keyword from numeric value
        i = i.split()
        #add horizontal if forward
        if i[0] == 'forward':
            horizontal_position += int(i[1])
            depth += (int(i[1]) * aim)
        #add depth/aim if up, subtract if down    
        elif i[0] == 'up':
            aim -= int(i[1])
        elif i[0] == 'down':
            aim += int(i[1])
    #multiply depth * horizontal position and return
    print(depth)
    print(horizontal_position)
    return horizontal_position*depth
        

with open('dataforAdventCode.txt', "r") as file:
    input = [x for x in file.read().split('\n')]

print(position_depth(input))

