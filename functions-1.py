def hi():
    print("Hello Guys!!!")

for i in range(10):
    hi()
####
def yil():
    import datetime
    return datetime.datetime.now().year

def yas():
    return yil() - 1987

print(yas())
####
def writeToConsole(text,number):
    return text * number
###
def yaziTura():
    import random
    print(random.random())
yaziTura()    
########################
def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if(sayi > 1):
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)
asalSayilariBul(10,30)
#############################
def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(2, sayi):
        if(sayi % i == 0): #mod
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(20))