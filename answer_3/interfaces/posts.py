from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    post_id = Column(Integer)
    title = Column(String)
    body = Column(Text)

    def __repr__(self):
        return f"<Post(id={self.id}, user_id={self.user_id}, post_id={self.post_id}, title={self.title})>"
