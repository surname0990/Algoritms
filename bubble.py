from random import randint
 
def bubble(array):
    for i in range(N-1): 
        print("i", i)
        for j in range(N-i-1):  
            print("j", j)
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
 
N = 10
a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
 
print(a)
bubble(a)
print(a)