
liste = ["1","3","a5","6"]
# just print int values.
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue
print("*************************")

stocks = {"StockName":"Samsung S20"}

def get(liste, key):
    try:
        return liste[key]
    except KeyError:
        return None
    
#result = get(stocks,"fiyat")
result = get(stocks,"StockName")
print(result)
