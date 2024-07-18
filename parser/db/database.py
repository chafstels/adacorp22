from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from parser.db.models import Product

DATABASE_URL = "postgresql://anton:1@localhost/data_wb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()
metadata.create_all(bind=engine)
Product.metadata.create_all(bind=engine)
