## Author - Thomas Uren

import csv

required =[]
completed =[]

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

    try:
        with open('book_collector.csv') as csvfile:
            file = csv.reader(csvfile)
            for row in file:
                if row[-1] == "r":
                    required.append(row)
    except FileNotFoundError:
        a=[]

    try:
        with open('book_collector.csv') as csvfile:
            file = csv.reader(csvfile)
            for row in file:
                if row[-1] == "c":
                    completed.append(row)
    except FileNotFoundError:
        a=[]

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
        finish_book()
    elif user_input == "R":
        require_books()
    elif user_input == "C":
        completed_books()
    elif user_input == 'E':
        print('Thanks for using the book collector!')
        file_output()
    else:
        print("INVALID INPUT!")
        print('TRY AGAIN!')
        print(required)
        menu()


def add_book():
    print('Please enter the name of the book you wish to add: ')
    book_to_add = input()
    while book_to_add == '':
        print('Invalid input! Try again.')
        print('Please enter the name of the book you wish to add: ')
        book_to_add = input()

    print('Please enter the name of the author of the book: ')
    author_to_add = input()
    while author_to_add == '':
        print('Invalid input! Try again.')
        print('Please enter the name of the author of the book: ')
        author_to_add = input()

    while True:
        print('How many pages does the book have?')
        try:
            pages_to_add = int(input())
            if pages_to_add < 0:
                print('Please enter a positive whole number.')
                continue
            if pages_to_add != '':
                pages_to_add = str(pages_to_add)
                break
        except ValueError:
            print('Please enter a valid whole number.')

    required.append([book_to_add,author_to_add,pages_to_add,'r'])
    print('{} by {} added to the list!'.format(book_to_add,author_to_add))
    menu()


def require_books():
    total_pages = 0
    total_books = 0
    if required != []:
        print('Books that are uncompleted:')
        a=[]
        for i in required:
            total_books += 1
            for j in i:
                a.append(j)
            print('{}.  {}  by  {}.     {} pages.'.format(total_books,a[0],a[1],a[2]))
            total_pages += int(a[2])
            a=[]
        print('{} books with {} pages.'.format(total_books, total_pages))
    else:
        print('You have no books you require to read. Enter some more at the main menu!')
    menu()


def completed_books():
    total_pages = 0
    total_books = 0
    if completed != []:
        print('All completed books:')
        a=[]
        for i in completed:
            total_books += 1
            for j in i:
                a.append(j)
            print('{}.  {}  by  {}.     {} pages.'.format(total_books, a[0], a[1], a[2]))
            total_pages += int(a[2])
            a=[]
        print('{} books with {} pages.'.format(total_books, total_pages))
    else:
        print('You have no completed book on the list.')
    menu()


def finish_book():
    book_exists = 0
    change_book = 0
    ### find book in list by name. send the book to the completed list with the r changed to a c.###
    print('What is the number of the book you wish to mark off?')
    try:
        marked_book = int(input())
        marked_book -= 1
        mark_off = required[marked_book]
    except ValueError:
        print('Please enter a valid number.')
    try:
        if mark_off in required:
            book_exists = 1
        if book_exists != 1:
            print('Book does not exist in required list. Please check the list and try again.')
        else:
            for i in required:
                i[3] = 'c'
                completed.append(i)
                required.remove(i)
                print('{} was marked off!'.format(i[0]))
    except IndexError:
        print('Invalid input. Check the list and try again.')

    menu()


def file_output():
    with open('book_collector.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, lineterminator='\n')
        for row in required:
            filewriter.writerow(row)
        for row in completed:
            filewriter.writerow(row)

main()
