ad_15 =  lambda x: x+15
multiply = lambda x,y: x*y
print(ad_15(10))
print(multiply(6,8))

def func_compute(n):
    return lambda x: x * n

result = func_compute(2)
print("Double the number of 15 =", result(22.5))

list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(list)
list.sort(key=lambda x: x[1])
print(list)

sort_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(sort_dict)
sort_dict.sort(key=lambda x: x['make'])
print(sort_dict)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lamda_f = lambda x: x % 2 ==0 
print("Lambda function:", lamda_f)
even_numbers = list(filter(lamda_f, nums))
print("Even numbers:", (even_numbers))

odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums) 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums)

square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums) 

starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('POLiGRAM'))

import datetime

now = datetime.datetime.now()
print(now)
year2 = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()
print(year2(now))
print(month(now))
print(day(now))
print(time(now))

chec_num = lambda x: str(x).replace('.','',1).isdigit()
print(chec_num(12345))
print(chec_num('num'))

fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

from functools import reduce

print(fibonacci_series(2))

print(fibonacci_series(5))  

print(fibonacci_series(6))  

print(fibonacci_series(9)) 
