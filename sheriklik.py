import psycopg2
def db_connect():
    conn = psycopg2.connect(
        host = "localhost",
        database = "farm",
        user = "postgres",
        password = "yangiobod84"
    )
    return conn
conn = db_connect()
cur = conn.cursor()
conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE kutubxona"
# )

# cur.execute(
#     """
#     CREATE TABLE book(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     price NUMERIC(10,2)
#     ) 
#     """
# )
# print("Creat table") 

# cur.execute(
#     "INSERT INTO book(name,price) VALUES('Binafsha shulasi',50000),('Qozichoqlar sukunati',80000),('Ikki eshik orasi',60000),('Odam bolish qiyin',40000),('Qizil ajdarho',70000),('Qalb iffati',55000)"
# )
# print("added")


# cur.execute(
#     # "SELECT * FROM book WHERE name IN ('Qalb iffati')"
#     # "SELECT * FROM book WHERE name NOT IN ('Qozichoqlar sukunati')"
# )
# rows = cur.fetchall()
# for i in rows :
#     print(i)


# cur.execute(
#     # "SELECT * FROM book WHERE price BETWEEN 60000 and 90000"
#     # "SELECT * FROM book WHERE name BETWEEN 'A' and 'K'"
#     # "SELECT id AS tartib_raqam FROM book "
# )
# rows = cur.fetchall() 
# for i in rows :
#     print(i)


# cur.execute(
#     "SELECT * FROM book WHERE name ILIKE 'Q%'"
# )
# cur.execute(
    # "SELECT * FROM book  LIMIT 2"
# )

# cur.execute(
    # "SELECT max(price) FROM book "
    # "SELECT min(price) FROM book "
    # "SELECT AVG(price) FROM book "
    # "SELECT COUNT(id) FROM book "
    # "SELECT SUM(price) FROM book "
# )






# rows = cur.fetchall()
# for i in rows :
#     print(i)




















