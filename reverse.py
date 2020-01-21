a=int(input("Enter a number: "))
t=a
r=0
while(a!=0):
    d=a%10
    r=(r*10)+d
    a=int(a//10)
print("Reverse of ",t,"is: ",r)