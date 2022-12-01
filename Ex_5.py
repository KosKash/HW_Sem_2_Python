#Алгоритм перемешивания списка
import random
in_list = ['a',2,'b',4,5,6,7,8]
out_list = []
while  len(out_list) != len(in_list):
    x = in_list[random.randint(0,len(in_list)-1)] 
    if x not in out_list:
        out_list.append(x)
print('Исходный список - {}\nПолученный список  - {}'.format(in_list,out_list))
    


