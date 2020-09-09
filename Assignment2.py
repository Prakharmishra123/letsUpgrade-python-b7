lst = list(range(2501))
count = 0
def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count == 2:
        return n
temp_list = list(filter(lambda n: prime(n),lst))
print(temp_list)
    
