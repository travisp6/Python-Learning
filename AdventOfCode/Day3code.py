#check power consumption by multiplying the gamma rate by the epsilon rate
#the gamma rate is the most common bit in each 'column' of data as a decimal
#the epsilon rate is the least common bit in each 'column' of data as a decimal
#input list of ones and zeros
#output power consumption (gamma rate * epsilon rate)

def power_consumption(number):
    #create empty list as power
    power = ''
    #take the total number of 1's and 0's in [0] from the list
    for i in range(0, len(number[0])):
        #create number of total 1 and 0 in i[x]
        position_one_1 = 0
        position_one_0 = 0
        for p in range(0, len(number)):
            if number[p][i] == '0':
                position_one_0 += 1
            else:
                position_one_1 += 1
        #if the value has more 1's append 1 to power list
        if position_one_1 > position_one_0:
            power += '1'
        #if the value has more 0's append 0 to power list
        else:
            power += '0'
    return power

with open('dataforAdventCode.txt', "r") as file:
    input = [x for x in file.read().split()]
print(power_consumption(input))





# print(int('110101101101',2))
# print(int('001010010010',2))






# print (int('10110', 2))
