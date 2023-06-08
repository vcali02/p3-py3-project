# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from db.models import (Base, Reader, Book, CheckedOutBook)

# if __name__ == '__main__':
#     pass

#     engine = create_engine('sqlite:///library.db')
#     Base.metadata.create_all(engine)
   
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     reader = session.query(Reader).first()