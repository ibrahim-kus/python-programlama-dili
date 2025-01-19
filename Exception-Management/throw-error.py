
# x = 20

# if x > 5:
#     raise Exception("x 5 den büyük olamaz.")

print("*********Check Str")

# def renklendir(text,renk):
#     if type(text) is not str:
#         raise TypeError("text must be str types")
    
# renklendir(10,10)

print("*********Faktoriyel*****")
def faktoriyel(x):
    x = int(x)
    if (x<0):
        raise ValueError("Negatif Değer")

    result = 1
    for i in range(1,x+1):
        result *= i

    return result

for i in [6,3,'2a',7,-3,9]:
     try:
         x = faktoriyel(i)
     except ValueError as e:
         print(e)
         continue
     else:
         print(x)
