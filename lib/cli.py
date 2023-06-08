from datetime import datetime
#allows you to print formatted text, render tables
from rich.console import Console
#allows you to define custom color
from rich.theme import Theme
#defines table columns, add rows of data, and customize the style and appearance of the table
from rich.table import Table
#supports features like headers, lists, bold and italic text, code blocks etc
from rich.markdown import Markdown
#used to create a SQLAlchemy engine (which represents the interface to the database)
#takes a database URL as an argument and returns an engine instance that can be used to establish a connection to the database
from sqlalchemy import create_engine
#takes an Engine instance as an argument and when called creates a new Session bound to that Engine
#perform CRUD
from sqlalchemy.orm import sessionmaker
#importing the base classes
from db.models import *

#creates a SQLAlchemy engine object using the create_engine function
#argument 'sqlite:///library.db' specifies the connection URL to the SQLite database
engine = create_engine('sqlite:///library.db')
#sessionmaker object is created using the sessionmaker class
#bind parameter binds/connects the sessionmaker to the database engine
Session = sessionmaker(bind=engine)
#creates a new session by calling the sessionmaker object, which returns an instance of the Session class
session = Session()

MARKDOWN = """
# Library Management System

Please select your desired function by number
1. List all readers
2. List all books
3. Add a new reader
4. Add a new book
5. Checkout a book
6. Check in a book
7. Delete a reader
8. Delete a book
9. Exit
"""

#console object is created using the Console class from the rich.console module
console = Console()
#md object is created using the Markdown class from the rich.markdown module
md = Markdown(MARKDOWN)


class CLI:
    def __init__(self):
        self.start()

    #entry point for the cli
    #connecting the numbers to the methods
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
                self.delete_reader()
            elif choice == "8":
                self.delete_book()
            elif choice == "9":
                exit = True


    def list_readers(self):
        #queries the Reader table 
        #result is stored in the readers variable as a list
        readers = session.query(Reader).all()
        #creates a new Table object with the title "Readers"
        #show_header=True means the table will display a header row
        #header_style="bold" set style of the header text to "bold"
        table = Table(title="Readers", show_header=True, header_style="bold")
        #adds a column to the table with the header text "ID"
        #justify="center" means content in this column will be centered
        #style="cyan" specifies the text color for this column
        table.add_column("ID", justify="center", style="cyan")
        #adds a column to the table with the header text "Name"
        #style="yellow" sets the text color for this column
        table.add_column("Name", style="yellow")
        #loop that iterates over each reader object in the readers list
        for reader in readers:
            #adds a new row to the table for each reader
            #str(reader.id) reader's ID converted to a string
            #reader.reader_name is the reader's name
            table.add_row(str(reader.id), reader.reader_name)
        #print the table
        console.print(table)

    def list_books(self):
        books = session.query(Book).all()
        table = Table(title="Books", show_header=True, header_style="bold")
        table.add_column("ID", justify="center", style="cyan")
        table.add_column("Title", style="yellow")
        for book in books:
            table.add_row(str(book.id), book.book_title)
        console.print(table)

    def add_reader(self):
        #prompts the user to enter the name of the reader 
        #and stores the input in the name variable
        name = input("Enter reader name: ")
        #creates a new Reader object using the provided reader name
        #reader_name attribute is set to the value of the name variable
        reader = Reader(reader_name=name)
        #adds the reader object to the current session
        session.add(reader)
        #commits the changes made in the session to the database
        session.commit()
        print("Reader added successfully.")

    def add_book(self):
        title = input("Enter book title: ")
        book = Book(book_title=title)
        session.add(book)
        session.commit()
        print("Book added successfully.")

    def checkout_book(self):
        #prompts the user to enter the ID of the reader who wants to check out a book
        # stores the input in the reader_id variable
        reader_id = input("Enter reader ID: ")
        #prompts the user to enter the ID of the book to be checked out
        #stores the input in the book_id variable
        book_id = input("Enter book ID: ")
        #prompts the user to enter the checkout date in the format "YYYY-MM-DD"
        #stores the input in the checkout_date variable
        checkout_date_str = input("Enter checkout date (YYYY-MM-DD): ")
        checkin_date_str = input("Enter checkin date (YYYY-MM-DD): ")
        #take str variable as 1st argument in next two lines
        checkout_date = datetime.strptime(checkout_date_str, "%Y-%m-%d")
        checkin_date = datetime.strptime(checkin_date_str, "%Y-%m-%d")
        

       #retrieves the Reader instance with the reader_id using the get() method
       #get(keyname, value)
       #searches for a Reader object with a matching ID in the database
        reader = session.get(Reader, reader_id)
        book = session.get(Book, book_id)

        #checks if both the reader and book objects exist
        if reader and book:
            #new CheckedOutBook object is created with the provided reader_id, book_id, and checkout_date
            checked_out_book = CheckedOutBook(
                reader_id=reader_id,
                book_id=book_id,
                checkout_date=checkout_date,
                check_in_date=checkin_date
            )
            #adds the checked_out_book object to the session.
            session.add(checked_out_book)
            #commits to database
            session.commit()
            print("Book checked out successfully.")
        else:
            print("Invalid reader or book ID.")

    def checkin_book(self):
        #enter the ID of the book to be checked in
        #stores the input in the book_id variable
        book_id = input("Enter book ID: ")
        #queries the database to get the CheckedOutBook instance associated with the provided book_id
        #filter_by() method to filter the query results based on the book_id column
        #first() method gets the first result matching the filter criteria
        #assigns it to the checked_out_book variable
        checked_out_book = session.query(CheckedOutBook).filter_by(book_id=book_id).first()
        #checks if a CheckedOutBook instance was found for the given book_id
        #if match exists, execute if block
        if checked_out_book:
            #called to delete the checked_out_book object from the session
            session.delete(checked_out_book)
            #commit changes to the database
            session.commit()
            print("Book checked in successfully.")
        else:
            print("Invalid book ID.")

    
    def delete_reader(self):
        #enter the ID of the reader to be deleted
        #stores the input in the reader_id variable
        reader_id = input("Enter reader ID: ")
        #gets the Reader object associated with the provided reader_id
        reader = session.get(Reader, reader_id)

        #if a Reader instance matches the given reader_id execute the if block
        if reader:
            session.delete(reader)
            session.commit()
            print("Reader deleted successfully.")
        else:
            print("Invalid reader ID.")

    def delete_book(self):
        book_id = input("Enter book ID: ")
        book = session.query(Book).get(book_id)

        if book:
            session.delete(book)
            session.commit()
            print("Book deleted successfully.")
        else:
            print("Invalid book ID.")
    
if __name__ == "__main__":
    cli = CLI()