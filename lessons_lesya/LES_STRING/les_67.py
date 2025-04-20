import re
name = input()
replacements = str.maketrans({"a": "97", "A": "65", "e": "101", "E":"69", "i": "105", "I": "73", "o": "111", "O": "79", "u": "117", "U": "85", "y": "121", "Y": "89"})
res = name.translate(replacements)
print(res)


"""Задача на замена гласных букв на их коды из unicoda ("a" = 97)"""

"""s = input()
for i in 'aeiouyAEIOUY':
    s = s.replace(i, str(ord(i)))
print(s)"""