a=int(input())
b=int(input())
c=int(input())
if a + b <= c or a + c <= b or b + c <= a:
    print("трикутник існує")
elif a != b and a != c and b != c:
    print("трикутник різносторонній")
elif a == b == c:
    print("трикутник рівносторонній")
else:
    print("різнобедрений")