
class Product:    
    # attribute, property
    def __init__(self,name,price):  #Constructor
        #self.name = "Iphone 15"
        self.name = name
        self.price = price
    
    # method
    def get_product(self):
        return f"Ürün adı{self.name} fiyat : {self.price}"

p1 = Product("Iphone 16", 100) # Instance
p2 = Product("Iphone 17", 200)

urunler = [p1,p2]

for urun in urunler:
    print(urun.get_product())

#result = type(p1)
#result = p1.name + ' ' + p2.name
#print(result) 