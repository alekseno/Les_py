import re
num = input()
result = re.findall(r"(\b\d{13}\b)", num)
print(*result)

"""1. Получает от пользователя строку, содержащую ISBN номеров (и ошибок в них).
2. Использует регулярные выражения, чтобы найти все корректные ISBN.
3. Выводит список найденных корректных ISBN в одну строку, через пробел.
4. Примечание: Как минимум один корректный номер есть!"""