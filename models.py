from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from load_csv import engine

Base = declarative_base()

class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    product = Column(String)
    region = Column(String)
    revenue = Column(Float)

Base.metadata.create_all(engine)
print("Tables created")
