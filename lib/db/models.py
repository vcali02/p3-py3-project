from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Float,  DateTime, ForeignKey)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


#readers can read many books
class Reader(Base):
    __tablename__ = 'readers'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    reader_name = Column(String())


    def __repr__(self):
        return f"Id: {self.id}, " \
        + f"Reader: {self.reader_name}"
    
    #relationship
    #val.checked_out_books
    #take val, go to the checked out books list
    #and find the ones where she is in there
    checked_out_books = relationship("CheckedOutBook", back_populates="reader")




#books can be read by many readers
class Book(Base):
    __tablename__ = 'books'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    book_title = Column(String())

    def __repr__(self):
        return f"Id: {self.id}, " \
        + f"Book: {self.book_title}"
    
    #relationship
    #harry_potter.checked_out
    #take book, go to the checked out books list
    #and find the ones where the book is in
    checked_out = relationship("CheckedOutBook", back_populates="books")


    
#connecting table that says, this reader, has this book. 
class CheckedOutBook(Base):
    __tablename__ = 'checked_out_books'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    checkout_date = Column(DateTime())
    check_in_date = Column(DateTime())

    #this is the foreign key that connects reader table to checked out book table
    #this is the foreign key that connects book table to checked out book table
    reader_id = Column(Integer(), ForeignKey('readers.id'))
    book_id = Column(Integer(), ForeignKey('books.id'))


    #relationship between reader and checked out books
    #harry_potter.reader is the book and who has it checked out
    reader = relationship("Reader", back_populates="checked_out_books")

    #val.books is the reader the books they have checked out
    books = relationship("Book", back_populates="checked_out")