from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://u118790815_fastapi:Fastapi123@217.21.91.1/u118790815_fastapi")
meta = MetaData()
conn = engine.connect()