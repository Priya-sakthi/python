#input from users
n=int(input("Enter the number of terms:"));
#first two trems
a=0;
b=1;
c=0;2

if(n<=1):
    print("enter the number above 2")
 #using loop generate fibonocci series
while c<n:
    print(a)
    sum=a+b
    a=b;
    b=sum;
    c+=1


