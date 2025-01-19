try:
    x = int(input("x:"))
    y = int(input("y:"))
    print(x+y)
except:
    print("hata oluştu. Girdiğiniz verileri kontrol ediniz.")

print("**************EXCEPTION TYPES*************")
# Attribute error
"hi".upper()
#"hi".Upper() # Attribute error

print("**************EXCEPTION HANDDLING*************")
while True:
    try:
        x = int(input("x:"))
        y = int(input("y:"))
        print(x+y)
    #except ZeroDivisionError:
        print("hata oluştu. ZeroDivisionError")
    #except ValueError:
    #    print("hata oluştu. ValueError")
    except (ZeroDivisionError, ValueError) as e:
        print("ZeroDivisionError veya ValueError  hatası oluştu.")
        print(e)
    except Exception as e:
        print("Bilinmeyen bir hata oluştu")
        print(e)
    else:
        break # herşey yolundaysa çık. hata alındıysa süreci devam ettir.
    finally:
        print("db connection close.")
