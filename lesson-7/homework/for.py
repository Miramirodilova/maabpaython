def maximum (a,b):
    if a > b:
        return a
    return b

print(maximum(3,8))

def sum (numbers):
    total = 0 
    for x in numbers:
        total += x
    return total 
print(sum((8,3,2,0,7)))   

def multipy (nums):
    result = 1
    for i in nums:
        result *= i
    return result

print(multipy((8,2,3,-1,7)))

def reverses(text):
    result = ""
    for x in text:
        result = x + result
    return result

print(reverses("1234abcd"))

def factorial (n):
    if n == 1 or n == 0:
        return 1
    else:
      return  n * factorial(n-1)
print(factorial(5))

ef weather (num):
    if num in range(3,9):
        print (f'{num} is in the range')
    else:
        print('The number is outside the given range.')  

weather(5) 

def cuonnt(str):
    str = {'UPPER_CASE':0 , 'LOWER_CASE':0}
    for c in str:
      if str.islower():
        str ['UPPER_CASE'] +1    
      elif str.islower():
         str['LOWER_CASE']+1
      else:
         pass
print('MoHira',str)     

x = []

def nums (l):
   for i in l:
    if i  not in x:
      x.append(i)
   return x    
print(nums([1,2,3,3,3,3,4,5])) 

def weather (n):
    if n == 1:
        return False
    if n == 2:
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True
print(weather(-1))

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def given_n(n):
    if  n % 2 == 0:
        print('even number')
    else:
        print('not even')

given_n(8)

def p_num (n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
         sum += 1
    return sum == 1

print(p_num(8))


def palindrome(string):
    left_pos = 0
    right_pos = len(string) - 1
    
    while right_pos >= left_pos:
        if string[left_pos] != string[right_pos]:
            return False
        
        left_pos += 1
        right_pos -= 1
    
    return True

print(palindrome('azi')) 
print(palindrome('aza'))  


import string
import sys

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    
    str_set = set(str1.lower())
    
    return alphaset <= str_set

print(ispangram('The quick brown fox jumps over the lazy dog')) 


item = [n for  n in input().split('-')]
item.sort()
print('-'.join(item))

def p_value():
   l = list()
   for i in range(1,21):
    l.append(i**2)
    print(l)
p_value

def make_bold():
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic():
    def wrapped():
        return "<i>" + fn() + "</i>"
    return make_italic

def make_underline():
    def wrapped():
        return "<u>" + fn() + "</u>"
    return make_underline

make_bold
make_italic
make_underline

my_code =  "print('hello_worod')"

code = """"print(strength in the night
poeple beautiful
strength in the night)"""

exec (my_code)

def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b
    return add

func = test(4)
print(func(4))  


def abs():
    x = 2
    y = 1
    str1 = 'w3school'
    print('python lesson')  
print(abs.__code__.co_nlocals)  

ri = lambda a: a + 15
print(ri(10))
rin = lambda x, y: x * y
print(rin(12, 4))
