from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv(".env")

conexion = mysql.connector.connect(
   host = os.getenv("DB_HOST"),
   port = int(os.getenv("DB_PORT")),
   user = os.getenv("DB_USER"),
   password = os.getenv("DB_PASSWORD"),
   db = os.getenv("DB_NAME"),
)