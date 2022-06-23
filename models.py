from database import Base
from sqlalchemy import String,Boolean,Integer,Column

class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(225),nullable=False,unique=True)
    description=Column(String(500))
    amount=Column(Integer,nullable=False)
    on_offer=Column(Boolean,default=False)

    def __repr__(self):
        return f"<Item name={self.name} price={self.amount}>"
    