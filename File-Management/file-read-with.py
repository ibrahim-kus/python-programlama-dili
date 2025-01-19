#File Read With _With

#file = open("log.txt",encoding="utf-8")

#print(file.read())

#file.close()

##########
with open("log.txt",encoding="utf-8") as file: # not need close.
    #print(file.read())
    #print(file.read(10))
    #print(file.tell())
    for i in file:
        print(i, end="") # end boşlukları kaldırmak için 
print("\n#####WRITE FILE####")

with open("dosya.txt","w",encoding="utf-8") as fileW: # w write mode create new file
    fileW.write("Ali Kuş\n")
    fileW.write("İbrahim Kuş\n")

with open("dosya.txt",encoding="utf-8") as fileW: # not need close.
    for i in fileW:
        print(i, end="")

print("\n#####ADD TO EXIST FILE####")  # a append mode, # r+ both read and write
with open("dosya2.txt","a", encoding="utf-8") as fileA:
    fileA.seek(0) # not execute because mode a.
    fileA.write("üçüncü satir\n")

print("\n#####UPDATE EXIST FILE####")

# with open("brands.txt","a") as fileU:
#     fileU.write("6-bmw")

with open("brands.txt", "r+", encoding="utf-8") as fileU:
    fileU.seek(0)
    fileU.write("1-Toyota")