#find the life support rating by multiplying the oxygen generator rating by the CO2 scrubber rating
#the oxygen generator rating is found by taking data from the first column that has more 1's or 0's at [0], 
#then using that data to keep the column that has more 1's or 0's at [1] ect til 1 number is left
#if 1 and 0 are qually common, keep the value with a 1 in the position being considered
#CO2 is least common value, keeping 0 if equal
#input: data from the list
#output: life support ratint (oxygen generator decimal * CO2 scrubber rating decimal)

def life_support_rating(number):
    the_count = 0
    #cycle through numbers to see if there are more 1 or 0
    while len(number) > 1:
        #create empty oxygen_one/zero lists
        #create count of more ones/zeroes
        oxygen_one = []
        oxygen_zero = []
        the_ones = 0
        the_zeroes = 0
        for i in range(0, len(number)):
            #if more 1s add to 1's count
            if number[i][the_count] == '1':
                the_ones += 1
                oxygen_one.append(number[i])
            #if more 0's add to 0's count
            elif number[i][the_count] == '0':
                the_zeroes += 1
                oxygen_zero.append(number[i])
        #once through all the numbers use oxygen_one/zero list based one which is greater
        if the_ones > the_zeroes:
            number = oxygen_one
        elif the_ones == the_zeroes:
            number = oxygen_one
        else:
            number = oxygen_zero
        #repeat steps using next [i] in new list
        the_count += 1
    return number

def life_support_rating2(number):
    the_count = 0
    #cycle through numbers to see if there are more 1 or 0
    while len(number) > 1:
        #create empty oxygen_one/zero lists
        #create count of more ones/zeroes
        oxygen_one = []
        oxygen_zero = []
        the_ones = 0
        the_zeroes = 0
        for i in range(0, len(number)):
            #if more 1s add to 1's count
            if number[i][the_count] == '1':
                the_ones += 1
                oxygen_one.append(number[i])
            #if more 0's add to 0's count
            elif number[i][the_count] == '0':
                the_zeroes += 1
                oxygen_zero.append(number[i])
        #once through all the numbers use oxygen_one/zero list based one which is greater
        if the_ones < the_zeroes:
            number = oxygen_one
        elif the_ones == the_zeroes:
            number = oxygen_zero
        else:
            number = oxygen_zero
        #repeat steps using next [i] in new list
        the_count += 1
    return number

with open('dataforAdventCode.txt', "r") as file:
    input = [x for x in file.read().split()]
print(life_support_rating(input))
print(life_support_rating2(input))