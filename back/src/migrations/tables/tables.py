# models.py
from sqlalchemy import Table, Column, String, MetaData, Integer, Date

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("email", String, primary_key=True, nullable=False),
    Column('name', String, nullable=False),
    Column('birthdate', Date, nullable=True),  # Nuevo campo birthdate de tipo Date
    Column('is_active', Integer, default=1)  # Nuevo campo is_active
)
