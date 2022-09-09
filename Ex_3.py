#Список и k последовательности (1+1\k)**k
num = int(input('Input N '))
num_list = []
for i in range(num):
    i+=1
    num_list.append((1+1/i)**i)
res = sum(num_list)
print('{}: {}'.format(num,round(res,3)))

