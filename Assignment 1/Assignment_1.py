## Author - Thomas Uren

import csv

global user

def main():
    try:
        with open('name.csv') as namefile:
            user = []
            file = csv.reader(namefile)
            for row in file:
                user.append(row)
        for i in user:
            print('Welcome back',", ".join(i),'!')
    except FileNotFoundError:
        print('Hello!')
        user = input('Please enter your name: ')
        with open('name.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, lineterminator='\n')
            filewriter.writerow([user])
        print('Welcome {}!'.format(user))
    menu()

def menu():
    print('')
    print('Would you like to:')
    print("(A)dd a book.")
    print("Complete (B)ook.")
    print("(R)equired list  of books.")
    print("(C)ompleted list of books.")
    print("(E)xit program.")
    user_input = str.capitalize(input())

    if user_input == "A":
        print('Adding books')
        add_book()
    elif user_input == "B":
        print('Completing book!')
    elif user_input == "R":
        print('Requiring book...')
    elif user_input == "C":
        print('All completed books')
    elif user_input == 'E':
        print('Exit...')
    else:
        print("INVALID INPUT!")
        print('TRY AGAIN!')
        menu()

def add_book():
    while True:
            print('Please enter the name of the book you wish to add: ')
            book_to_add = input()
            if book_to_add != '':
                break
            else:
                print('Invalid input! Try again.')

    while True:
            print('Please enter the name of the author of the book: ')
            author_to_add = input()
            if author_to_add != '':
                break
            else:
                print('Invalid input! Try again.')

    while True:
            print('How many pages does the book have?')
            pages_to_add = input()
            if pages_to_add != '':
                break
            else:
                print('Invalid input! Try again.')



main()

# def add_author():
#     print('Please enter the name of the author of the book: ')
#     author_to_add = input()
#     if author_to_add != '':
#         add_author()