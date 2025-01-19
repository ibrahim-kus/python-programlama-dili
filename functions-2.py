#default parameter
def usAlma(taban,us=2):  # default parameter 2  if not enter second parameter.
    return taban ** us 

print(usAlma(5))
print(usAlma(4,3))

#keyword arguments
def fullName(name: str,surname: str) -> str:
    return f"your name is {name} {surname}"

print(fullName(surname="kus",name="ibrahim")) # keyword arguments

# Değişken sayıda parametre  *args -> tuple
def toplam(*args):
    print(args)
    print(type(args))
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(toplam(10,20,30,40))

# Keyword Args kwargs  => dictionary
def display_user(*args):
    print(type(args))
    print(args)
display_user()
def display_user(**kwargs):
    #print(type(kwargs))
    #print(kwargs) 
    for key, value in kwargs.items():
        print(f"{key}: {value}")   

display_user(uname="ibrahim", email="aaa@aa.com")