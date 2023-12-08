from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    freebies = relationship("Freebie", backref="dev")

    def received_one(self, item_name):
        for freebie in self.freebies:
            if freebie.item_name == item_name:
                return True
        return False

    def give_away(self, other_dev, freebie):
        if freebie in self.freebies:
            freebie.dev = other_dev


