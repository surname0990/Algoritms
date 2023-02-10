a = int(input("Введите 1-е натуральное число: "))
b = int(input("Введите 2-е натуральное число: "))
sa = a; sb = b
while a != b:
   if a>b: a -= b
   else: b -=a
 
print("НОД(%d, %d) = %d"%(sa,sb,a))