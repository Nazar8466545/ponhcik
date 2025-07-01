run=True
while run:
    
    number = int(input("выберите путь"))
    if number ==1:
        print("Гравець знаходить скарб")
    elif number ==2:
        print(" Гравець знаходить вихід з печери")
    elif number ==3:
        print(" Гравець потрапляє в пастку ")
    else:
        print("такого пути нету.")
        run=False
print("hello")