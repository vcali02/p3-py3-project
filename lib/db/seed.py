from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Reader, Book, CheckedOutBook

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///library.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    #Add delete methods for Reader and Book to clear the database before each seeding
    session.query(Reader).delete()
    session.query(Book).delete()
    session.query(CheckedOutBook).delete()
    #Initialize faker
    fake = Faker()


    ####CREATE A LIST OF READERS####
    #empty lost for readers
    readers = []
    #create for loop that creates 50 readers
    for _ in range(random.randint(10, 25)):
        reader = Reader(
        reader_name=f"{fake.name()}"
    )

    #add and commit to save readers
    session.add(reader)
    session.commit()
    #append the reader to the reader array
    readers.append(reader)


    ####CREATE A LIST OF BOOK TITLES####
    #list of book titles
    book_titles = ["The Maidens" , "All The Missing Girls", "The House Across the Lake", "Just the Nicest Couple", "The House in the Pines", "The Last Mrs. Parrish", "The Good Girl", "The Woman in the Window", "The Midnight Library", "The Girls in the Garden", "The Silent Patient", "Local Woman Missing", "Where the Crawdads Sing", "The Hunting Party", "Gone Girl", "Whisper Network", "The Butterfly House", "When She Was Good", "The Better Sister", "One by One", "Verity", "Then She Was Gone", "Wrong Place Wrong Time", "Invisible Prey", "The Four Agreements"]
    
    #create an empty book array
    books = []
    #loop that iterates over the reader
    for reader in readers:
        #loop that iterates 1-3 times, to give the reader between 1-3 books to their name
        for _ in range(random.randint(10, 25)):
            book = Book(
                #generate book instances that are random based on the provided list book_titles
                book_title = random.choice(book_titles)
            )
            session.add(book)
            session.commit()
            books.append(book)

    
    ####CREATE A LIST OF CHECKED OUT BOOKS W. CHECK OUT AND CHECK IN DATES####
    checked_out_books = []
    for reader in readers:
        for _ in range(random.randint(10, 25)):
            checked_out = CheckedOutBook(
                checkout_date = fake.date_this_year(),
                check_in_date = fake.date_this_year(),
                reader_id = reader.id,
                book_id =  random.choice(books).id
            )
            checked_out_books.append(checked_out)
    
    session.bulk_save_objects(checked_out_books)
    session.commit()
    session.close()
 
    