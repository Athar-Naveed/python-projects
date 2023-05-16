import sqlite3
def create_db():
    con = sqlite3.connect(database=r"ims.db")
    cur = con.cursor()
    cur.execute("create table if not exists product (pro_id integer primary key autoincrement, pro_name text not null, pro_price integer not null,pro_quantity integer not null)")
    con.commit()

create_db()