#Take the sum of three consecutive depth measurements and compare it to the next three consecutive depth measurements and see if there is an increase
#example: [1,2,3,4,5,6] compare 1+2+3 to 2+3+4 
#input: i+(i+1)+(i+2)
#output: increase or decrease
#stop when there are not enough depth measurements to add 3 of them together


def depth_measurement(number):
    position = 0
    increase = 0
    #use a while loop to add the number of increases and decreases
    while position < len(number)-1:
        for i in range(1, len(number)):
            if number[i-1] + number[i] + number[i+1] < number[i] + number[i+1] + number[i+2]:
                print (number[i-1] + number[i] + number[i+1])
                print (number[i] + number[i+1] + number[i+2])
                increase += 1
                position += 1
                print(increase)
            else:
                position += 1
    return increase

list1 = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]

print(depth_measurement(list1))
