
pin_number="1234"
count=100
a=input()
if a==pin_number:
    if count>=0:
        n=int(input())
        if n>count:
            print("cannot withdraw")
        else:
            print(n)
else:
    print("your pin number is error ")