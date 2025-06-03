# models.py
from sqlalchemy import Table, Column, String, MetaData, Integer

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("email", String, primary_key=True, nullable=False),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=True)  # Nuevo campo age
)