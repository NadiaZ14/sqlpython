import sqlalchemy
print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("mysql+pymysql://root:password@localhost/film_library", echo=False, future=True)

with engine.connect() as conn:
    result = conn.execute(
        text("""update films set name = 'nadiatest' where id = F0001""")
    )
    conn.commmit()

#customer_number = (input("12345"))

#with engine.connect() as conn:
    #result = conn.execute(text("SELECT item_id FROM loaned_items"))
    #for row in result:
        #print(f"item_id {row.item_id}")

#conn.commit()





#with engine.connect() as conn:
    #result = conn.execute(
        #text("""select user_id, item_id, date_borrowed, date_due from loaned_items inner join films
       # on loaned_items.items_id = films.id where loaned_items.user_id = :id"""),
        #{"id": customer_number})
    #for row in result:
        #print(f"name: {row.name}  user_id: {row.user_id} film:")