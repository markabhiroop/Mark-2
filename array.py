a=int(input(""))
b=int(input(""))
if (a<b):
    print("Not enough numbers")
else:
    x =list(range(1,a+1))
    y=list(x[:b])
    d=sum(y)
    print(d)
