# for => list
numbers = [1,3,4,5,6,7,8]
for i in numbers:
    print(i)

my_tuple = [(1,2),(3,4),(5,6)]
for a,b in my_tuple:
    print(a,b)
print("######");
my_dictionary = {"07":"Antalya","34":"İstanbul"}
for x in my_dictionary.values():
    print(x);
for x in my_dictionary.keys():
    print(x);
for x in my_dictionary.items():
    print(x);

print("######");
phones = ["iphone 12", "samsung5","iphone 15","iphone 13"]
for phone in phones:
    index = phone.find('iphone')
    if index > -1:
        print(phone)

print("######")
items = [
    {"itemName":"Hp", "price":1000},
    {"itemName":"Samsung", "price":2000},
    {"itemName":"dell", "price":1500},
]
for item in items:
    print(f"{item['itemName']} price {item['price']}")

print("###### WHILE ########################")

print("###### RANGE ########################")
for i in range(1,100,2):
    print(i)
rng = range(10) 
result = list(rng)
print(result)
print("###### ENUMERATE ########################")
#index sağlar
brands = ["opel","bmw","togg","fiat"]

obj1 = enumerate(brands,1)
print(type(obj1))
print(list(list(obj1)))

for index,value in enumerate(brands,1):
    print(f"{index}--{value}")

print("###### ZIP ########################") #merge lists than one more 
numbers = [100,200,300]
students = ["Ahmet", "Ayşe", "Hayriye"]
print(list(zip(numbers,students)))


