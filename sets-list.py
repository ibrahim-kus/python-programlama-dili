
fruits = {"apple","banana","strawberry"}

print(fruits)

fruits.add("blueberry")
print(fruits)

result = "banana" in fruits
print(result)

fruits.remove("apple") #raise an error
fruits.discard("blueberry")

print(fruits)
