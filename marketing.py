import psycopg2

def db_connect():
    conn = psycopg2.connect(
        host = "localhost",
        database = "patients",
        user = "postgres",
        password =  "yangiobod84"
    )
    return conn



conn  = db_connect()
cur = conn.cursor()
conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE market"
# )
# print("👌")


# cur.execute(
#     """
#     CREATE TABLE products(
#     id SERIAL PRIMARY KEY,
#     p_name VARCHAR(100),
#     p_price NUMERIC(10,2)
#     )
#     """
# )
# print("👌")

# cur.execute(
#     "INSERT INTO products(p_name , p_price) VALUES('Xiomi17promax','17999999')"
# )

# cur.execute(
#     "SELECT * FROM products WHERE p_name ILIKE 'X%'"
# )
# cur.execute(
#     "SELECT * FROM products  LIMIT 2"
# )
# cur.execute(
    # "SELECT max(products) FROM products "
    # "SELECT min(products) FROM products "
    # "SELECT AVG(p_price) FROM products "
    # "SELECT COUNT(id) FROM products "
    # "SELECT SUM(p_price) FROM products "
    # "SELECT * FROM phones WHERE brand NOT IN ('SAMSUNG') "






# )
# rows = cur.fetchall()
# for i in rows :
#     print(i)





























