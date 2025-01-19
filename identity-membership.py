#identity operator
x = [2,4,6]
y = [2,4,6]
z = y 

print(x is y) #false because of memory address
print(x is not y)

print(z is y)

# membership operator
print(2 in x)
print(2 not in x)