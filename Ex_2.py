#Набор произведений
import math #Все мы используем читы :)

n = int(input("Input N "))
res_list = []
for i in range(n):
    res_list.append(math.factorial(i+1)) 

print('{}: {}'.format(n,res_list))

