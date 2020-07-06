b=(int(input("enter a variable")))
c=(int(input("enter b variable")))
r=1
while r>0:
      q=b/c
      r=b%c
      b=c
      c=r
print("gcd=",b)
      
