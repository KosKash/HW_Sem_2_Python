#Набор произведений
def fact(num):
    n = 1
    res = 1
    while num > n-1:
        res *= n
        n+=1
    return res



n = int(input("Input N "))
res_list = []
for i in range(n):
    res_list.append(fact(i+1)) 

print('{}: {}'.format(n,res_list))


