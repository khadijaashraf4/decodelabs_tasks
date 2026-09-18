"""
Bonus verification script: connects to the RDS MySQL instance through the
local SSH tunnel and prints the Interns table contents.

SETUP:
  1. Open the SSH tunnel first (in a separate terminal, keep it running):
       ssh -i "decodeLabs-key.pem" -L 3306:<RDS_ENDPOINT>:3306 ubuntu@<EC2_PUBLIC_IP>
  2. Install the dependency:
       pip install pymysql
  3. Set your DB password as an environment variable instead of hardcoding it:
       Windows (PowerShell):  $env:DB_PASSWORD = "your_password_here"
       macOS/Linux:           export DB_PASSWORD="your_password_here"
  4. Run:
       python connect.py

No real credentials are stored in this file — the password is read from the
environment so it's safe to commit this script to a public repo.
"""

import os
import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="admin",
    password=os.environ.get("DB_PASSWORD", ""),
    database="decodelabs_db",
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM Interns;")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
