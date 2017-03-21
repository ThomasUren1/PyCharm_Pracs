# Author - Tom Uren

towrite = input("Please enter your name: ")

with open('name.txt', mode="w") as file:
    file.write(towrite)


