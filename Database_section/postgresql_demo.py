import psycopg2

def create(tb):
    conn=psycopg2.connect("dbname = 'db_demo' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS {} (item TEXT,quantity INTEGER,price REAL)".format(tb))
    conn.commit()
    conn.close()

def view(table):
    conn=psycopg2.connect("dbname = 'db_demo' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("SELECT * from {}".format(table))
    cur.execute("SELECT count(*) from {}".format(table))
    r=cur.fetchall()
    conn.commit()
    conn.close()  
    return r
create('test')
val=(view('test'))
for i in val:
    print(i)


