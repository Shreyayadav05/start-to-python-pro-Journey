n=int(input())
a= n // 10
b=n%10
sum_digits = a+b
if sum_digits == 7:
    print("Special Number")
elif a == 7  or b ==7:
    print("Special Number")
elif(n%7==0):
    print("Special Number")
else:
    print("Normal Number")
