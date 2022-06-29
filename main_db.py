from dotenv import load_dotenv, find_dotenv
import os
import psycopg2
load_dotenv(find_dotenv())

#database variables
PASSWORD = os.environ.get("PASSWORD")
HOST_ADDR = os.environ.get("HOST_ADDR")
SSL_MODE = os.environ.get("SSL_MODE")
SSL_CERT = os.environ.get("SSL_CERT")
SSL_KEY = os.environ.get("SSL_KEY")
SSL_ROOTCERT= os.environ.get("SSL_ROOTCERT")
ROOTUSER = os.environ.get("ROOTUSER")
DB_NAME = os.environ.get("DB_NAME")
PORT = 5432

#Use db variables to create Dsn connection string
connectParamDsn = f"""
    sslmode=verify-ca sslrootcert={SSL_ROOTCERT} sslcert={SSL_CERT} sslkey={SSL_KEY} hostaddr={HOST_ADDR} port={PORT} user={ROOTUSER} dbname={DB_NAME} password={PASSWORD}
    """

# Create connection instance using psycopg2
conn = psycopg2.connect(connectParamDsn)