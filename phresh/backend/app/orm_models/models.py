from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.sql.sqltypes import Numeric

Base = declarative_base()

class Cleanings(Base):
    __tablename__ = "cleanings"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, index=True)
    description = Column(Text, nullable=True)
    cleaning_type = Column(Text, nullable=False, server_default="spot_clean")
    price = Column(Numeric(10, 2), nullable=False)
