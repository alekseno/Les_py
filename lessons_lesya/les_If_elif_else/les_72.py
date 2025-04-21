complex = input()
meaning = int(input()) # значение
if complex == "Двигатель":
    if meaning < 30:
        print("Критически низкий уровень топлива!")
    elif meaning > 70:
        print("Топливо в норме, продолжайте миссию.")
    elif  30 <= meaning <=70:
        print("Заправьте двигатель для продолжения.")
    
         