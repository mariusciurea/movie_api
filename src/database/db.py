"""
Requirements
------------
    pip install sqlalchemy
    pip install mysql-connector-python

db URL general template:
<dialect>+<driver>://<username>:<password>@<host>:<port>/<database>
------------------
    MySql
    mysql_db_url = "mysql://<username>:<password>@<hostname>:<port>/<database>"
    mysql_db_url = "mysql+mysqlconnector://<username>:<password>@<hostname>:<port>/<database>"

    PostgreSQL
    postgresql_db_url = "postgresql://<username>:<password>@<hostname>:<port>/<database>"
    "postgresql+psycopg2://<username>:<password>@<hostname>:<port>/<database>"

Get username and port from SQL server
--------------------
    CREATE DATABASE test_docker;
    USE test_docker;

    SHOW VARIABLES WHERE Variable_name = 'port';
    SELECT user();
"""
import os

import mysql.connector
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

# load_dotenv("env_var/backend.env")

mysql_url = 'mysql+mysqlconnector://root:Changeme_123@localhost:3306/test_api'

engine = create_engine(mysql_url)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()




