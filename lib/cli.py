# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from db.models import (Base, Reader, Book, CheckedOutBook)


# class CLI:
#     def __init__(self, user_input):
#         self.readers = [reader for reader in session.query(Reader)]
#         self.books = [book for book in session.query(Book)]
#         self.checked_out_books = [checkedout for checkedout in session.query(CheckedOutBook)]
#         self.name = user_input
#         self.start()


#     def start(self):
#         print(' ')
#         print(f'***** Welcome To The Library {self.name} *****')
#         print(' ')


    

# if __name__ == '__main__':
    

#     engine = create_engine('sqlite:///library.db')
#     Base.metadata.create_all(engine)
   
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     #ONE TO MANY

#     ####GET READERS BOOKS#### 
#     #Grab the first reader
#     reader = session.query(Reader).first()

#     #Use session.query to filter through Books and get the reader's books

#     #print out the reader's books



#     ####GET BOOKS READ BY SELECT READERS####
#     #use session.query to grab the first pet

#     #use session.query and filter to get the reader associated with the book

#     #print out the book's readers


#     #MANY TO MANY

#     #use session.query to get the first owner

#     #use session.query to grab the books

#     #print the books


#     #####check notes




#################################################################


from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.markdown import Markdown
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import *

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

MARKDOWN = """
# Library Management System

Please select your desired function by number
1. List all readers
2. List all books
3. Add a new reader
4. Add a new book
5. Check out a book
6. Check in a book
7. Exit
"""

console = Console()
md = Markdown(MARKDOWN)


class CLI:
    def __init__(self):
        self.start()

    def start(self):
        exit = False
        while not exit:
            console.print(md)
            choice = input("Selection: ")
            if choice == "1":
                self.list_readers()
            elif choice == "2":
                self.list_books()
            elif choice == "3":
                self.add_reader()
            elif choice == "4":
                self.add_book()
            elif choice == "5":
                self.checkout_book()
            elif choice == "6":
                self.checkin_book()
            elif choice == "7":
                exit = True

    def list_readers(self):
        readers = session.query(Reader).all()
        table = Table(title="Readers", show_header=True, header_style="bold", box=console.box.MINIMAL_HEAVY_HEAD)
        table.add_column("ID", justify="center", style="cyan")
        table.add_column("Name", style="yellow")
        for reader in readers:
            table.add_row(str(reader.id), reader.reader_name)
        console.print(table)

    def list_books(self):
        books = session.query(Book).all()
        table = Table(title="Books", show_header=True, header_style="bold", box=console.box.MINIMAL_HEAVY_HEAD)
        table.add_column("ID", justify="center", style="cyan")
        table.add_column("Title", style="yellow")
        for book in books:
            table.add_row(str(book.id), book.book_title)
        console.print(table)

    def add_reader(self):
        name = input("Enter reader name: ")
        reader = Reader(reader_name=name)
        session.add(reader)
        session.commit()
        print("Reader added successfully.")

    def add_book(self):
        title = input("Enter book title: ")
        book = Book(book_title=title)
        session.add(book)
        session.commit()
        print("Book added successfully.")

    def checkout_book(self):
        reader_id = input("Enter reader ID: ")
        book_id = input("Enter book ID: ")
        checkout_date = input("Enter checkout date (YYYY-MM-DD): ")
        checkin_date = input("Enter checkin date (YYYY-MM-DD): ")

        reader = session.query(Reader).get(reader_id)
        book = session.query(Book).get(book_id)

        if reader and book:
            checked_out_book = CheckedOutBook(
                reader_id=reader_id,
                book_id=book_id,
                checkout_date=checkout_date,
                check_in_date=checkin_date
            )
            session.add(checked_out_book)
            session.commit()
            print("Book checked out successfully.")
        else:
            print("Invalid reader or book ID.")

    def checkin_book(self):
        book_id = input("Enter book ID: ")
        checked_out_book = session.query(CheckedOutBook).filter_by(book_id=book_id).first()

        if checked_out_book:
            session.delete