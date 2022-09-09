#Сумма цифр
numbers = str(input("Введите число "))
x = len(numbers)
num = []
   
for i in range(len(numbers)):
    num.append(numbers[i])
if ',' in num:  
    num.remove(',')
if '.' in num:
    num.remove('.')
if '-' in num:
    num.remove('-')

res_num = []
for i in range(len(num)):
    res_num.append(int(num[i]))
res = sum(res_num) 
print('{} : {}'.format(res_num,res))

