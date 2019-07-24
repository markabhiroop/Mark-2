v=list(str(input("")))
a=int(v[0])
b=int(v[2])
if (a<b):
    print("Not enough numbers")
else:
    x =list(range(1,a+1))
    y=list(x[:b])
    d=sum(y)
    print(d)
