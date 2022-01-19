#create a list of the length of each word in a string
def words(string):
    return list(map(len, string.split()))
string1 = "this is a sentence"
print(words(string1))

#make a function that takes a list and prints it without commas
def thelist(commalist):
    print(*commalist, sep = '')
list1 = [1,2,3,4,5,6]
thelist(list1)

#return words in a list that start with only the specified letter
def theword(string, letter):
    splitter = string.split()
    startswith = [i for i in splitter if i[0] == letter]
    print(startswith)
theword('here we have a letter h', 'h')

#concatenate two lists together with a designated connector
def combinewords(a,b,connector):
    return [i+connector+ii for (i,ii) in zip(a,b)]
alist = ['animal','bug','dinosaur']
blist = ['dog','ant','Trex']
print(combinewords(alist,blist,'--'))

#use enumerate on a list
def enumerated(list1):
    return list(enumerate(list1))
listenumerated = ['a','b','c']
print(enumerated(listenumerated))

#