
programming_languages = ["python","C#","Java","js"]

result = programming_languages
result = programming_languages[0:2]
print(result)

programming_languages[-1] = "Php"
result=programming_languages
print(result)

result = programming_languages + ["Go", "Delphi"]
print(result)

# is exist 
result = "python" in programming_languages
print(result)

for i in programming_languages:
    print(i)

#delete
del programming_languages[-1]
print(programming_languages)