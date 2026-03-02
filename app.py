import os
import psycopg2

db_url = os.environ["DATABASE_URL"]

conn = psycopg2.connect(db_url)

print("DB CONNECTED OK")
