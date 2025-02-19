list1=[1, 2, 3, 5, 7, 8, 9, 10]
list2=[1, 2, 4, 8, 9]

intersect = list(filter(lambda x: x in list2,list1))
print(intersect)

array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
result = sorted(array_nums, key=lambda i: 0 if i == 0 else -1 / i)
print(result)

numbers=[1, 2, 3, 5, 7, 8, 9, 10]
odd_nums = len(list(filter(lambda x: x % 2 !=0,numbers)))
even_numbers = len(list(filter(lambda x: x%2 ==0,numbers)))

print(even_numbers)

numbers = [1, 2, 3, 5, 7, 8, 9, 10]
odd_nums = len(filter(lambda x: x % 2 != 0, numbers)) 
even_numbers = len(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days = filter(lambda day: len(day) == 6, weekdays)

for d in days:
    print(d)

l=[1, 2, 3]
l2=[4, 5, 6]

add= map(lambda x,y: x + y, l ,l2)
print(list(add))

nums = (1, 2, 3, 4, 5, 6, 7)
print(nums)
result = map(lambda x: x+x+x,nums)
print(list(result))

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

result = map(lambda x,y,z: x+y+z,nums1,nums2,nums3)
print(list(result))

color = ['Red', 'Blue', 'Black', 'White', 'Pink']
print(color)
result =  list(map(list,color))
print(result)

bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(bases_num,index)
result = list(map(pow,bases_num,index))
print(result)

def square(n):
    return n*n
nums = nums = [4, 5, 2, 9]
result = map(square,nums)
print(list(result))

def convert(s):
    return str.lower(s), str.upper(s)
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
result = map(lambda c: convert(c)[0],chrars)
print(set(result))

def diff(a,b):
    return a+b, a-b

nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]

result = map(diff,nums1,nums2)

print(list(result))

nums_list = [1, 2, 3, 4]
nums_tuple = (0, 1, 2, 3)

print(nums_tuple,nums_list)

result_tuple = tuple(map(str,nums_tuple))
result_list = list(map(str,nums_list))
print(nums_tuple)
print(nums_list)

n = 10
def fibonacci_nums(x=0, y=1):
    while True:
        yield x
        x, y = y, x + y

fib_gen = fibonacci_nums()
result = [next(fib_gen) for _ in range(n)]

print("Fibonacci numbers:", result)

square = lambda x: x * x

squared_result = list(map(square, result))
print("Squared Fibonacci numbers:", squared_result)


def count_matching_pairs(list1, list2):
    matching = map(lambda x, y: x == y, list1, list2)
    return sum(matching)

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 0, 4, 6]

result = count_matching_pairs(list1, list2)
print(f"Number of matching pairs: {result}")


def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)

marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

print(marks)

print(list_of_dicts(marks))

def covert (str):
    result = map(list,str)
    return list(result)
colors = ["Red", "Green", "Black", "Orange"]
print(colors)
print(covert(colors))

def covert (pairs):
    result = list(map(''.join,pairs))
    return (result)
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(colors)
print(covert(colors))

mixed_case_strings = ["Hello", "w3resource", "Python", "Filter", "Learning"]
result = list(filter(lambda char: char.isupper() ,''.join(mixed_case_strings)))
print(result)

names = ["Elita", "Vitold", "Audovacar", "Kerensa", "Ramana", "Iolanda", "Landyn"]
def starts_with_vowel(name):
    return name[0].lower() in ['a', 'e', 'i', 'o', 'u']

vowel_names = list(filter(starts_with_vowel, names))
print(vowel_names)

students = [
    {"name": "Denis Helio", "age": 17, "grade": 97},
    {"name": "Hania Mehtap", "age": 16, "grade": 92},
    {"name": "Kelan Stasys", "age": 17, "grade": 90},
    {"name": "Velvet Mirko", "age": 16, "grade": 94},
    {"name": "Delores Aeneas", "age": 17, "grade": 100}]
def hig_grade (students):
    return students['grade'] >= 95
hig_gradee = list(filter(hig_grade,students))
print(hig_gradee)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print(numbers)

prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)

words = ["Red", "Green", "Orange", "White", "Black", "Pink", "Yellow"]
def has_more_5(words):
    return len(words) > 5
result = list(filter(has_more_5,words))
print(result)

from datetime import datetime
date_strings = ["2023-07-11", "2022-02-22", "2024-05-11", "2025-12-31", "2021-01-01"]
print(date_strings)
dates = [datetime.strptime(date, "%Y-%m-%d") for date in date_strings]

current_date = datetime.now()
print("Current date:",current_date)

def is_date_in_future(date):
    return date > current_date

dates_in_past = list(filter(is_date_in_future, dates))

filtered_date_strings = [date.strftime("%Y-%m-%d") for date in dates_in_past]
print("\nCheck if a date is in the future!")
print(filtered_date_strings)

class Book:
    def __init__(self,title,authior,pages):
       self.title =  title
       self.author = authior
       self.pages = pages

    def summary(self): 
        return f'author:{self.author},pages: {self.pages},title:{self.title}'        
    
first_book = Book('the helan','someone',123)
print(first_book.summary())    


