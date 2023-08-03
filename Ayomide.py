FINE_PER_DAY = 500/7  # 500 naira per week fine for late submission from the due date
BORROW_PERIOD = 15  # Due date will be 15 DAYS from the date of borrow.

data = [
    {"TITLE": "Ayomide Akpata", "BOOK CODE": "AKPRR1", "AUTHOR": "Author A", "AVAILABILITY": "BORROWED", "BORROWER ID": "UGCS001", "DUE DATE": "12-06-2021"},
    {"TITLE": "MECHANICS-1", "BOOK CODE": "AKPRR2", "AUTHOR": "Author B", "AVAILABILITY": "BORROWED", "BORROWER ID": "UGCS001", "DUE DATE": "16-06-2021"},
    {"TITLE": "LIS-220", "BOOK CODE": "AKPRR3", "AUTHOR": "Author C", "AVAILABILITY": "AVAILABLE", "BORROWER ID": "", "DUE DATE": ""},
    {"TITLE": "MORDERN COMPUTING", "BOOK CODE": "AKPRR4", "AUTHOR": "Author D", "AVAILABILITY": "BORROWED", "BORROWER ID": "UGCS002", "DUE DATE": "16-06-2021"},
    {"TITLE": "Operating Systems -WILEY", "BOOK CODE": "AKPRR5", "AUTHOR": "Author E", "AVAILABILITY": "AVAILABLE", "BORROWER ID": "", "DUE DATE": ""},
    {"TITLE": "PYTHON PROG.", "BOOK CODE": "PESRR6", "AUTHOR": "Author F", "AVAILABILITY": "AVAILABLE", "BORROWER ID": "", "DUE DATE": ""}
]

def getDate(a):
    import datetime
    now = datetime.datetime.now() + datetime.timedelta(days=a)
    return now.strftime('%d') + '-' + now.strftime('%m') + '-' + now.strftime('%Y')

def fine(a, b, cost_per_day):
    from datetime import datetime
    date_format = '%d-%m-%Y'
    d1 = datetime.strptime(a, date_format)
    d2 = datetime.strptime(b, date_format)
    diff = d2 - d1
    Fine = diff.days * (cost_per_day)
    if Fine < 0:
        return 0
    else:
        return Fine

def aval():
    print('The available books are:')
    available_books = [book["TITLE"] for book in data if book["AVAILABILITY"] == 'AVAILABLE']
    print(available_books)

def borrow():
    borrower_id = input('please input the ID: ')
    borrowed_books = [book["TITLE"] for book in data if book["BORROWER ID"] == borrower_id]
    if borrowed_books:
        print('The borrowed books are:')
        print(borrowed_books)

    def validd():
        global code
        code = input('ENTER THE BOOK CODE OF THE BOOK TO BE BORROWED: ')
        if code not in [book["BOOK CODE"] for book in data]:
            print('Please enter a valid book code.')
            validd()

    validd()
    book = next((book for book in data if book["BOOK CODE"] == code), None)
    if book["AVAILABILITY"] == 'BORROWED':
        print('This book is already borrowed.')
    else:
        book["AVAILABILITY"] = 'BORROWED'
        book["BORROWER ID"] = borrower_id
        book["DUE DATE"] = getDate(BORROW_PERIOD)
        print(f'Title: {book["TITLE"]}, Book Code: {book["BOOK CODE"]}, Author: {book["AUTHOR"]}, Availability: {book["AVAILABILITY"]}, Borrower ID: {book["BORROWER ID"]}, Due Date: {book["DUE DATE"]}')
        print("Book borrowed successfully.")

def give_back():
    borrower_id = input('please input the ID ')
    borrowed_books = [book["TITLE"] for book in data if book["BORROWER ID"] == borrower_id]
    if not borrowed_books:
        print('No books have been borrowed!')
    else:
        print('The borrowed books are:')
        print(borrowed_books)

        def valid():
            code = input('Enter the book code of the book to be returned: ')
            book = next((book for book in data if book["BOOK CODE"] == code), None)
            if book and book["BORROWER ID"] == borrower_id:
                book["AVAILABILITY"] = 'AVAILABLE'
                print('\nBook returned successfully.')
                print('LATE SUBMISSION FINE: ', fine(book["DUE DATE"], getDate(BORROW_PERIOD), FINE_PER_DAY), 'Naira')
                book["BORROWER ID"] = ''
                book["DUE DATE"] = ''
            else:
                print('Please enter a valid book code.')
                valid()

        valid()

def show_indigenous_authors():
    print("Indigenous Nigerian Authors:")
    indigenous_authors = [
        {"NAME": "Chinua Achebe", "BOOKS": ["Things Fall Apart", "Arrow of God", "No Longer at Ease"]},
        {"NAME": "Wole Soyinka", "BOOKS": ["Death and the King's Horseman", "A Dance of the Forests", "The Man Died: Prison Notes of Wole Soyinka"]},
        {"NAME": "Chimamanda Ngozi Adichie", "BOOKS": ["Purple Hibiscus", "Half of a Yellow Sun", "Americanah"]},
        # Add more indigenous Nigerian authors and their books here
        # ...
    ]
    for author in indigenous_authors:
        print(f"{author['NAME']}: {', '.join(author['BOOKS'])}")

def add_book():
    title = input("Enter the title of the book: ")
    book_code = input("Enter the book code: ")
    author_name = input("Enter the author's name: ")
    availability = input("Enter the availability (AVAILABLE/BORROWED): ")
    borrower_id = input("Enter the borrower ID: ")
    due_date = input("Enter the due date (dd-mm-yyyy): ")
    
    new_book = {"TITLE": title, "BOOK CODE": book_code, "AUTHOR": author_name, "AVAILABILITY": availability, "BORROWER ID": borrower_id, "DUE DATE": due_date}
    data.append(new_book)
    print("Book added successfully.")

# start
while True:
    print('')
    print("********************************************************************")
    print('                      LIBRARY MANAGEMENT SYSTEM SOFTWARE            ')
    print("Date: ", getDate(0))
    print("********************************************************************")
    print('')
    print("Enter 1. To Display all the books")
    print('Enter 2. To Display the available books.')
    print("Enter 3. To Borrow a book")
    print("Enter 4. To return a book")
    print("Enter 5. To Show Indigenous Nigerian Authors")
    print("Enter 6. To Add a Book")
    print("Enter 7. To Quit")
    opt = int(input())
    if opt == 1:
        print("TITLE      | BOOK CODE | AUTHOR           | AVAILABILITY | BORROWER ID | DUE DATE")
        for book in data:
            print(f"{book['TITLE']:<20} {book['BOOK CODE']:<10} {book['AUTHOR']:<16} {book['AVAILABILITY']:<13} {book['BORROWER ID']:<12} {book['DUE DATE']}")
    elif opt == 2:
        aval()
    elif opt == 3:
        borrow()
    elif opt == 4:
        give_back()
    elif opt == 5:
        show_indigenous_authors()
    elif opt == 6:
        add_book()
    elif opt == 7:
        exit()
    else:
        print('Please enter a valid input.')

    print("")
    input("Press ENTER..")
