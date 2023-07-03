from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from get_config import config

SQLALCHEMY_DATABASE_URL = "postgresql://" + config['PSQL_USERNAME'] + ":" + config['PSQL_PASSWD'] \
                         + config["PSQL_HOSTNAME"] + "/" + config["PSQL_DB"]


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()