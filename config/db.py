from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://u118790815_fastapi:Fastapi123@sql787.main-hosting.eu/u118790815_fastapi")
meta = MetaData()
conn = engine.connect()