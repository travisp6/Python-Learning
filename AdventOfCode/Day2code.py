#calculate the horizontal position and depth of a given a list of forward/down/up movements then multiply them together
#example: forward 3, down 5, up 1
#input: horizontal position (foward) and depth (up/down)
#output: horizontal postion * depth

def position_depth(number):
    #create horizontal position and depth counter
    horizontal_position = 0
    depth = 0
    #check if keyword is forward, down, or up
    for i in number:
        #split keyword from numeric value
        i = i.split()
        #add horizontal if forward
        if i[0] == 'forward':
            horizontal_position += int(i[1])
        #add depth if up, subtract if down    
        elif i[0] == 'up':
            depth -= int(i[1])
        elif i[0] == 'down':
            depth += int(i[1])
    #multiply depth * horizontal position and return
    print(depth)
    print(horizontal_position)
    return horizontal_position*depth
        

with open('dataforAdventCode.txt', "r") as file:
    input = [x for x in file.read().split('\n')]

print(position_depth(input))
