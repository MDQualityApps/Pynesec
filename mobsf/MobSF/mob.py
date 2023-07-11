import sqlite3;
import hashlib;


conn = sqlite3.connect("userdata.db")
cur = conn.cursor


cur.execute("""
CREATE TABLE IF NOT EXISTS loginuser(
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    passw VARCHAR(255) NOT NULL,

)
""")

username1, password1 = "pynesectech", hashlib.sha256("pyne".encode()).hexdigest()

cur.execute("INSERT INTO loginuser (username, passw) VALUES (?,?)",(username1, password1))
conn.commit()