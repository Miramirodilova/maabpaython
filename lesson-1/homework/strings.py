print('hello world')

str1 = 'welcome \tto my blog'
str2 = 'welcome to\t my \nblog'
print(str1)
print(str2)

text1 = """welcome to
 my blog.
 This is
  for classX"""
print(text1)

gap1 = 'welcome to my blog'
gap2 = 'welcome to my \nblog'
print(gap1)
print(gap2)

empt_str = ' '
print(empt_str)

name_blog = "this is Amit's blog"
print(name_blog)

index_text = 'Mohira'
print(index_text[:3])

index_text = 'Mohira'
a = ' '
for i in range(len(index_text)):
    a+=index_text[i]
print(a)

name1 = 'moh'
name2 = 'hira'
name3 = name1[:1]+name2[len(name1)-1:]
print(name3)

print('my_name '+'Mohira' *2)

print("num" *3 + "text"+ '7')

sentence  = 'welcome to my website below'
print(sentence.find('to'))
print(sentence.find('10'))
print(sentence.find('to,my'))
print(sentence.find('my'))

sentence  = 'welcome to my website below'
print(sentence[-1])
print(sentence[9])

textt = 'i am using for loop'
for i in textt:
    print(i)
