a=int(input())
b=int(input())
rem=a%b 
rema=b%a 
if((a%b)<(b%a)):
    print(a%b)
else:
    print(b%a)
