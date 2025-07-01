cost = 6500
if cost < 1000:
    print("знижок немає")
elif cost < 2000:
    print("знижка 2%")
elif cost < 5000:
    print("знижка 5%")
else:
    print("знижка 10%")