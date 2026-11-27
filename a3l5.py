num = int(input("enter a number to be checked"))
f = False
if num>1:
    for i in range(2,num):
       if(num%i)==0:
          f = True
          break

    
if f:
    print(num, "this number is not a prime number")
else:
    print(num,"this is a prime number")

