from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    address = Column(Text) 
    phone = Column(String)
    website = Column(String)
    company = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, username={self.username})>"

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data['id'],
            name=data['name'],
            username=data['username'],
            email=data['email'],
            address=str(data['address']),
            phone=data['phone'],
            website=data['website'],
            company=data['company']['name']
        )