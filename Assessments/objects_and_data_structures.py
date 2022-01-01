'''
numbers: 1 2 3
Strings: 'hello'
Lists: [List,one,two,3]
Tuples: (1,2,3)
Dictionaries: ['one':1, 'two':2, 'three':3]
'''
st = 'Print e, reverse string, print o.'
print(st[6])
print(st[::-1])
print(st[-2])

#Build this list [0,0,0] two separate ways.
list1 = [0,0,0]
list2 = [0]*3
print(list1)
print(list2)

#Reassign 'hello' to say 'goodbye'
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

#sort the list
list4 = [5,2,7,3,2,6,7]
print(sorted(list4))

#grab 'hello' from the dictionary
dict1 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(dict1['k1'][2]['k2'][1]['tough'][2])

#use a set to find unique values of a list

list5 = [325,6,2,6,4,4,4,4,6,3,2,1,6,7]
print(set(list5))