lst = [1,3,4,5,7,8,1,3,5,7,1,3,4,7,8,5]
n = 0
for i in lst:
    if n==0 and i==1 or n==1 and i==1 or n==2 and i==5:
        n+=1
if n==3:
    print("It's a Match")
else:
    print("it's Gone")
