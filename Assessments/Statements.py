string1 = 'Print only words that stat with s in this sentence.'

for i in string1.split():
    if i[0] == 's':
        print(i)

# #print all even numbers 0 to 10
print(list(range(0,11,2)))

# #create a list of all numbers between 1 and 50 divisible by 3.
print([x for x in list(range(0,51)) if x%3 == 0])

string2 = 'Print every word that has an even number of letters'
for i in string2.split():
    if len(i) %2 == False:
        print(i)

#fizz=%3, buzz=%5, fizzbuzz=%3 and %5
for i in range(1,50):
    if i %5 == 0 and i %3 == 0:
        print('fizzbuzz')
    elif i %5 == 0:
        print('buzz')
    elif i %3 == 0:
        print('fizz')
    else:
        print(i)

string3 = 'Create a list of the first letters of every word in this string'
print([i[0] for i in string3.split()])

