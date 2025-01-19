import module # Way 1 

result = module.sayi

#print(result)

result = module.sayilar
result = module.stock
result = module.stock["colour"]

print(result)

import module as m  # way 2 

result1 = m.sayi

from module import sayi, sayilar # way 3  part of module 

from module import * # way 4 

result4 = toplama(4,6)
