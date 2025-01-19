
f = open("log.txt","r",encoding='utf-8') # default read mod

print(f)
#print(f.read())
#print(f.read()) # ikinci read için okunacak birşey kalmaz. Cursor mantığıyla çalışır.

f.seek(0) # Cursoru en başa al.

print(f.readline()) # Just Read row
print(f.readlines())  # List 
print(f.closed)  # Dosya kapalı mı ?
f.close() #Kapat
print(f.closed)