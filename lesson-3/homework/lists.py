food =["rice", "beans"]
food.append("Broccoli")
print (food)
food.extend(["bread", "pizza"])
print (food)
print(food[:2])
print(food[-1])
breakfast ="eggs, fruit, orange juice".split(", ")
print (breakfast)
print(len(breakfast))
lengths = [len(item) for item in breakfast]
print (lengths)
