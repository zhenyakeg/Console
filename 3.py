__author__ = 'student'
import sys
for x in sys.argv:
    with open(x,'r') as file:
        print(file.read())
