
n=(int(input("enter the number of stars")))
for i in range(0,n):
      for j in range(n-i):
            print(end=" ")
      for k in range(i):
            print("* ",end="")
      print()


