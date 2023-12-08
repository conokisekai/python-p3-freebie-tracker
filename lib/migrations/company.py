from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    devs = relationship("Dev", secondary='freebies', backref="companies")
    freebies = relationship("Freebie", backref="company")

    def give_freebie(self, dev, item_name, value):
        new_freebie = Freebie(dev=dev, company=self, item_name=item_name, value=value)
        return new_freebie

    @classmethod
    def oldest_company(cls):
        return cls.query.order_by(cls.founding_year).first()
