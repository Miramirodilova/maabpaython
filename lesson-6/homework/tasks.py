list1 = [1,1,2]
list2 = [2,3,4]

result1 = [item for item in list1 if item not in list2]
result2 = [item for item in list2 if item not in list1]

un_commons = result1 +result2
print(un_commons)

list1 = [1,2,3]
list2 = [4,5,6]

result1 = [item for item in list1 if item not in list2]
result2 = [item for item in list2 if item not in list1]

un_commons = result1 +result2
print(un_commons)

list1 = [1,1,2,3,4,2]
list2 = [1,3,4,5]

result1 = [item for item in list1 if item not in list2]
result2 = [item for item in list2 if item not in list1]

un_commons = result1 +result2
print(un_commons)

def process_string(txt):
    vowels = 'aeiou'  # Unli harflar
    result = []  # Natija uchun ro'yxat

    for i in range(len(txt)):
        result.append(txt[i])  # Harfni natijaga qo'shish
        # Har uchinchi belgidan keyin "_" qo'shish
        if (i + 1) % 3 == 0 and i != len(txt) - 1:  # Oxirgi belgidan keyin "_" qo'shilmaydi
            if txt[i] not in vowels:  # Agar belgi unli bo'lmasa
                result.append('_')

    return ''.join(result)  

print(process_string('hello'))

  def process_string(txt):
    vowels = 'aoiue'
    results = []

    for i in range(len(txt)):
       results.append(txt[i])
       if (i + 1) % 3 == 0 and i != len(txt) -1:
          if txt[i] not in vowels:
             results.append('_')
    return ''.join(results)

print(process_string('hello'))

  def process_string(txt):
    vowels = 'aouie'
    results = []

    for i in range(len(txt)):
       results.append(txt[i])
       if (i + 1) % 3 == 0 and i != len(txt) -1:
         if txt[i] not in vowels:
          results.append('_')      
    return ''.join(results)

print(process_string('assalom'))  
