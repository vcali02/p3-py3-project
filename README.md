# Val's Library CLI App


Val's Library is a CLI application that allows a librarian to see a list of available books, see a list of library members, or readers, add new library members/readers, add new books, delete members/readers and books. 
This README file will explain how to use the application and how each function works.


## Installation and Prerequisites

To run the Val's Library app, you will need:


1.Python 3.5 or higher
2.SQLAlchemy
3.Rich Library 
4.Faker

You can install the required libraries by running the following command in your terminal:


```$ pipenv install``

Now that your environment is set up, run `pipenv shell` to enter it.

How to Use the App
To start the CoffeeIron app, `cd` into the `lib` directory, then run:

```$ python cli.py```


## Usage

Upon running the script, the user is greeted with the main menu. The user can select an option by entering the corresponding number.


## Files:

### cli.py

This file is super important for Val's Library App. It imports necessary modules such as create_engine and sessionmaker from SQLAlchemy, as well as custom classes from models.py. 

The CLI class is defined with methods such as start, add_book, and delete_reader to interact with the user by adding or deleting items. list_books displays a list of books available to checkout, and checkout_book allows the user to check out a book and prints out a message confirming the checkout process.


### models.py

The models.py file contains the database schema for Val's Library borrowing system. It defines three tables using SQLAlchemy: Reader, Book, and CheckedOutBook.

### seed.py

The seed.py file is used to populate the database with initial data. It imports the necessary modules and creates an instance of the engine and session to interact with the database. It then creates instances of the Book class, which represent the different books available for checkout at the library, and adds them to the database. 

### library.db

library.db is our SQLite database file that is used to store information about the drinks menu and orders. The database schema includes three tables: "readers", "books", and "checked_out_books".  

## Functions:


**start()**
The start function displays a message and prompts the user for input, which is then used to call other functions.
1. List all readers
2. List all books
3. Add a new reader
4. Add a new book
5. Checkout a book
6. Check in a book
7. Delete a reader
8. Delete a book
9. Exit

**list_readers()**
The list_readers function produces a table of all of the library members/readers

**list_books()**
Creates a table of all books available to checkout

**add_reader()**
This function creates a new reader/library member. 

**add_book()**
Allows the librarian to add new books to the available book list.

**checkout_book()**
checkout_book allows the librarian to check a book out for a reader/library member

**checkin_book()**
This function allows a librarian to check a book back into the books available for checkout list.

**delete_reader()**
Allows the librarian to delete a reader/library member

**delete_book()**
Allows the librarian to delete a book


## Models

Val's Library utilizes a one-to-many and many-many relationship schema, and it features three important models.


## References

[SQLalchemy](https://www.sqlalchemy.org/)

[Rich Documentation](https://rich.readthedocs.io/en/stable/introduction.html)

[Faker Documentation](https://faker.readthedocs.io/en/master/writing-docs.html)
