import sqlite3

def create():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def view(table):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    #cur.execute("SELECT * from {}".format(table))
    cur.execute("SELECT count(*) from {}".format(table))
    r=cur.fetchall()
    conn.commit()
    conn.close()  
    return r

val=(view('store'))
for i in val:
    print(i)


