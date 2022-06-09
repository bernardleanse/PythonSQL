import sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = engine = create_engine('postgresql://bernardleanse@localhost:5432/testing')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)
# This is what creates tables based on metadata
# generated from the child classes of Base


Session = sessionmaker(bind=engine)
# This is how we talk to the database custom made Session class...?

# Session = sessionmaker(), then when engine variable exists
# you can then go ahead and go Session.configure(bind=engine)

session = Session()

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
bernard = User(name='bernard', fullname='nah mate', nickname='bazzy')
session.add(ed_user)
session.add(bernard)

session.commit()

q = session.query(User)

ed = q.filter(User.name == "Ed Jones")

print(ed)




