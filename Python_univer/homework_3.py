
import math

n=70
print(); print("*"*n)
print("Лабораторна робота №3 - Цикли")
print("-"*n)
print("*"*n)

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


while True:
    print("Виберіть варіант відповіді: \n1 - ряд з точністю \n2  - кінцевий ряд \n3 - вихід з програми")
    
    number = input()
    if number == "1":
        s, sk, n= 1, 0, 0
        x = ""
        eps = ""
        while True:
            print("введіть значення x")
            x = input()
            if is_digit(x)==False:
                print("Ви ввели букву")
            else:
                x = float(x)
                break
            
        while True:
            print("введіть значення eps")
            eps = input()
            if is_digit(eps)==False:
                print("Ви ввели букву")
            else:
                eps = float(eps)
                break
        while math.fabs(s)>=eps:
            n = n+1;
            s = ((-1)**n)*(((x-(math.pi/4))**(2*n))/(math.factorial(2*n)))
            sk = sk + s
        print("SK = ", sk)
        print("N = ", n)   
    elif number =="2":
        s, sk, n= 1, 0, 0
        x = ""
        k = ""
        while True:
            print("введіть значення x")
            x = input()
            if is_digit(x)==False:
                print("Ви ввели букву")
            else:
                x = float(x)
                break
        while True:
            print("введіть значення k")
            k = input()
            if is_digit(k)==False:
                print("Ви ввели букву")
            else:
                k = int(k)
                break
        n = 1
        while n<=k:        
            s = ((-1)**n)*(((x-(math.pi/4))**(2*n))/(math.factorial(2*n)))
            sk = sk + s
            n = n+1;
        print("SK = ", sk)
    elif number == "3":
        print("Ви вийшли з програми")
        break
    else:
        print("\n\n\nТакого варіанта не існує\n\n\n")
