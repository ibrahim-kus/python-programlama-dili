
def passCheckerTr(parola):
    tr_character = "şçğüöıİ"

    for i in parola:
        if i in tr_character:
            raise TypeError("Exist tr character!!!")
    print("Valid Password")


parola = input("parola:")

try:
    passCheckerTr(parola)
except TypeError as e:
    print(e)