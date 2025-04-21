object = input().lower()
yes_no = ''
if object != "математика" and object != "физика" and object != "литература" and object != "биология":
    print("Попробуйте себя в разных сферах, чтобы найти своё призвание!")

if object == "математика":
    yes_no = input().lower()
    if yes_no == "да":
        print("Вам подойдёт профессия аналитика!")
    else:
        print("Вам подойдёт профессия программиста!")

if object == "физика":
    yes_no = input().lower()
    if yes_no == "да":
        print("Вам подойдёт профессия астронома!")
    else:
        print("Вам подойдёт профессия инженера!")

if object == "литература":
    yes_no = input().lower()
    if yes_no == "да":
        print("Вам подойдёт профессия писателя!")
    else:
        print("Вам подойдёт профессия редактора!")

if object == "биология":
    yes_no = input().lower()
    if yes_no == "да":
        print("Вам подойдёт профессия врача!")
    else:
        print("Вам подойдёт профессия эколога!")