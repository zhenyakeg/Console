__author__ = 'student'
# импортируем модуль
import sys

# выводим на экран список всех аргументов
s=0
for arg in sys.argv:
    if len(arg) == 3:
        s+=1
print (s)