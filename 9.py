a=int(input())
b=int(input())
if a % b == 0:
    print(a/b)
else:
    print("Не ділиться повністю")
    print("Залишок:",a%b)
    print("Ділене:" , a//b)