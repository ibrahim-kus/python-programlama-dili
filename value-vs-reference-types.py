#value types 
# x = 10 
# # y = 20 
# # x = y  # value copied
# #y= 30 # 
# print(x, y) 

# reference 
a = ["apple","armue"] 
b = ["apple","armut"] 
a = b # memory addres copied. 
a[0] = "pineapple" 
print(a, b) 

#list copy
list1 = [10,20]
list2 = list1.copy()  #Method1 addres not copied. 
list2 = list(list1)  #Method2 addres not copied.  
list2[0]=30
print(list1,list2) 