from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import declarative_base
import datetime as dt
import os

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String, nullable=False)
    order_items = Column(String, nullable=False)
    table_number = Column(Integer, nullable=False)

    def toJSON(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "order_items": self.order_items.split(", "),
            "table_number": self.table_number
        }
