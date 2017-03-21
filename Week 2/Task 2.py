# Author - Tom Uren
import csv

with open("name.txt", mode='r') as toread:
    file = toread.read()
print("Your name is ",format(file))