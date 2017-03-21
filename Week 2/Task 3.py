# Author = Tom Uren
result = 0;

with open("numbers.txt", mode='r') as file:
    for line in file:
        result = float(line) + result
print(result)



#