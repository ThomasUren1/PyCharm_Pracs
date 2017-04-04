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

    with open('book_collector.csv') as csvfile:
        file = csv.reader(csvfile)
        for row in file:
            if row[-1] == "r":
                required.append(row)

    with open('book_collector.csv') as csvfile:
        file = csv.reader(csvfile)
        for row in file:
            if row[-1] == "c":
                completed.append(row)

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
        print('Books that are uncompleted:')
        require_books()
    elif user_input == "C":
        print('All completed books:')
        completed_books()
    elif user_input == 'E':
        print('Thanks for using the book collector!')
        file_output()
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
            try:
                pages_to_add = float(input())
                if pages_to_add != '':
                    pages_to_add = str(pages_to_add)
                    break
            except ValueError:
                print('Please enter a number.')

    required.append([book_to_add,author_to_add,pages_to_add,'r'])
    menu()


def require_books():
    a=[]
    for i in required:
        for j in i:
            a.append(j)
        print("".join(a[0]),'by',"".join(a[1]),", Book has","".join(a[2]),"pages.")
        a=[]
    menu()


def completed_books():
    a=[]
    for i in completed:
        for j in i:
            a.append(j)
        print("".join(a[0]),'by',"".join(a[1]),", Book has","".join(a[2]),"pages.")
        a=[]
    menu()


def finish_book():
    print('WORK IN DIS')
    ### find book in list by name. send the book to the completed list with the r changed to a c.###
    print('What is the name of the book you wish to mark off?')
    marked_book = input()
    for i in required:
        if marked_book in i:
            book_exists = 1
    if book_exists != 1:
        print('Book does not exist in list. Please check the list and try again.')
    else:
        for i in required:
            if marked_book in i:
                change_book = 1
            if change_book == 1:
                i[3] = 'c'
                completed.append(i)
                required.remove(i)

    menu()


def file_output():
    with open('book_collector.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, lineterminator='\n')
        for row in required:
            filewriter.writerow(row)
        for row in completed:
            filewriter.writerow(row)

main()
