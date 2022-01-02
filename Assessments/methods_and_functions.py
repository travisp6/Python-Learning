#return lesser of two numbers if both are even, but greater if one or both are odd
def lesser_greater(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b
print(lesser_greater(6,411))
print(lesser_greater(2,10))

#return true if both words begin with the same letter
def sameletter(a,b):
    if a[0] == b[0]:
        return True
    else:
        return False
print(sameletter('big','boy'))

#return true if the sum is 20 or if one of the numbers is 20, if not return false
def sum20(a,b):
    if a + b == 20:
        return True
    elif a == 20 or b == 20:
        return True
    else:
        return False
print(sum20(20,5))
print(sum20(15,5))
print(sum20(3,4))

#capitalize the first and fourth letters of a name
def macdonald(a):
    if a == a:
        return a[:3].capitalize() + a[3:].capitalize()
    else:
        pass
print(macdonald('macdonald'))

#reverse a sentence
def reverse(sentence):
    return ' '.join(sentence.split()[::-1])
print(reverse('I will be reversed'))

#return true if within 10 of 100 or 200
def within10(number):
    if number <= 100+10 and number >= 100-10:
        return True
    elif number <= 200+10 and number >= 200-10:
        return True
    else:
        return False
print(within10(90))
print(within10(209))
print(within10(19))
print(within10(210))

#return True if a 3 is next to a 3 in a list
def thirtythree(number):
    for i in range(0,len(number)-1):
        if number[i:i+2] == [3,3]:
            return True
    else:
        return False
print(thirtythree([7,3,6,3]))
print(thirtythree([7,3,6,3,3,7]))

#make the string have 3 characters for every original character
def makethree(words):
        return ''.join([i*3 for i in words])
print(makethree('words'))

#part of blackjack: add three numbers between 1 and 11. <=21 return sum. >21 bust. 11>21 change to 1
def blackjack(a,b,c):
    if a+b+c > 21 and 11 in (a,b,c):
        return a+b+c-10
    elif a+b+c <= 21:
        return a+b+c
    elif a+b+c >21:
        return 'bust'
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
