s=0
p=1
q=0
for n in range(1042000,702648265):
    s=0
    q=n
    c=0
    while q>0:
        q=q/10
        q=int(q)
        c=c+1
    q=n
    while q>0:
        p=q%10
        s+=pow(p,c)
        q=q/10
        q= int(q)
    if(s == n):
        print("The first armstrong number is: ",s)
        break
else:
    print("loop is ended")


