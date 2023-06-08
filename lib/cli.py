from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import (Base, Reader, Book, CheckedOutBook)

if __name__ == '__main__':
    

    engine = create_engine('sqlite:///library.db')
    Base.metadata.create_all(engine)
   
    Session = sessionmaker(bind=engine)
    session = Session()

    #ONE TO MANY

    ####GET READERS BOOKS#### 
    #Grab the first reader
    reader = session.query(Reader).first()

    #Use session.query to filter through Books and get the reader's books

    #print out the reader's books



    ####GET BOOKS READ BY SELECT READERS####
    #use session.query to grab the first pet

    #use session.query and filter to get the reader associated with the book

    #print out the book's readers


    #MANY TO MANY

    #use session.query to get the first owner

    #use session.query to grab the books

    #print the books


    #####check notes




