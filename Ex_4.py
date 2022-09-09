# -N to N промежуток

n = int(input("Input N "))
num_list = []
num = -n
while num <= n:
    num_list.append(num)
    num+=1
print(num_list)