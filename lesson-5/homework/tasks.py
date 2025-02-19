#exercise 1


scores = [('Mike', 75), ('Joe', 90), ('Beck', 85)]

students_above_80 = [name for name, score in scores if score > 80]

print(students_above_80)

  #task 2

def list_with_max_sum(tup):
 
    return max(tup, key=sum)

input_tuple = ([1, 2], [3, 4], [5, 6, 7])

result = list_with_max_sum(input_tuple)

print(result)

#task 3

people = [('Mike', 25), ('Joe', 31), ('Beck', 40)]

names_in_range = [name for name, age in people if 30 < age < 50]

print(names_in_range)

  #task 4

def even_odd_labels(numbers):
    return [(num, 'Even' if num % 2 == 0 else 'Odd') for num in numbers]

input_list = [1, 2, 3, 4]

result = even_odd_labels(input_list)

print(result)

  #task 5

def longest_string_with_largest_integer(tuples):
    return max(tuples, key=lambda x: (len(x[0]), x[1]))

input_list = [('apple', 5), ('banana', 4), ('cherry', 6)]

result = longest_string_with_largest_integer(input_list)

print(result)

  #task 6

def sort_events_by_date(tuples):

    return sorted(tuples, key=lambda x: x[0], reverse=True)

input_list = [('2024-12-01', 'Event A'), ('2025-01-01', 'Event B')]

result = sort_events_by_date(input_list)

print(result)

  #task 7

def highest_score(tuples):
    return max(tuples, key=lambda x: x[1])

input_list = [('Mike', 75), ('Joe', 90), ('Beck', 85)]

result = highest_score(input_list)

# Print the result
print(result)

  #task 8

def products_in_price_range(products):
    return [product for product in products if 50 <= product[1] <= 100]
input_list = [('product1', 45), ('product2', 60), ('product3', 120)]
result = products_in_price_range(input_list)
print(result)

  #task 9

def oldest_person(people):
    return max(people, key=lambda x: x[1])[0]
input_list = [('Mike', 25), ('Joe', 31), ('Beck', 40)]
result = oldest_person(input_list)
print(result)


  #task 10

def students_above_average(students):
    return [name for name, grades in students if sum(grades) / len(grades) > 80]
input_list = [('Mike', [85, 75, 90]), ('Joe', [70, 80, 60])]
result = students_above_average(input_list)
print(result)

  
