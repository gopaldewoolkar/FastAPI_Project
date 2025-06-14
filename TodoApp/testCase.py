# import secrets

# random_hex = secrets.token_hex(32)  # Generates a 64-character hex string (32 bytes)
# print(random_hex)

import psycopg2

conn = psycopg2.connect("dbname=TodoApplicationDatabase user=postgres password=necsws2025 host=localhost port=5432")
print("Connection successful!")
conn.close()