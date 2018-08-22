q=0
v=0
w=0
e=0
a=1
s=1
d=0
c=0
while v==0:
    s=1
    w=0
    a=a+1
    while a!=s:
        q = a%s
        s=s+1
        if q == 0:
            d = (s-1)
            w = w+d
    if w == a:
        print(w)
    








    
    

