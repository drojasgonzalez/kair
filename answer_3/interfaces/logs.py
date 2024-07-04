from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    level = Column(String(20))
    message = Column(Text)

    def __repr__(self):
        return f"<Log(id={self.id}, timestamp={self.timestamp}, level={self.level}, message={self.message})>"

    @classmethod
    def from_dict(cls, data):
        return cls(
            level=data.get('level'),
            message=data.get('message')
        )
