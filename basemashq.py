import psycopg2

def pro():
    biriktirish = psycopg2.connect(
        host = "localhost",
        database = "leftpro",
        user = "postgres",
        password = "yangiobod84"
    )
    return biriktirish

biriktirish = pro()
maxx = biriktirish.cursor()
biriktirish.autocommit = True

# 
# maxx.execute(
#     "CREATE DATABASE harakat"
# )
# print("Succes")

# maxx.execute(
#    """CREATE TABLE ismlar(
#    id SERIAL PRIMARY KEY ,
#    name VARCHAR(100)
#    ) 
#    """
# )
# print("Succes")

# maxx.execute(
#    """CREATE TABLE kasblar(
#    id SERIAL PRIMARY KEY ,
#    title VARCHAR(100)
#    ) 
#    """
# )
# print("Succes")

# maxx.execute(
#     "INSERT INTO ismlar(name) VALUES('Palankas')"
# )
# print("Succes")


# maxx.execute(
#     "INSERT INTO kasblar(title) VALUES('Bekorchi')"
# )
# print("Succes")

# maxx.execute(
#     "SELECT ismlar.name , kasblar.title FROM ismlar LEFT JOIN kasblar ON ismlar.id = kasblar.id"
# )

# rows = maxx.fetchall()
# for i in rows:
#     print(i)

                                                                                                  
#                                _ _ _ _ _ _ _           _ _ _ _ _ _ _          _ _ _ _ _ _ _ _ _ _ _                                   _ _ _ _ _ _ _                  _ _ _ _ _               _ _ _            _ _          _      
#            |                  |                       |                                 |                                                          |               /           \               |              |   \        |     
#            |                  |                       |                                 |                                                          |              /             \              |              |    \       |    
#            |                  |                       |                                 |                                                          |             |               |             |              |     \      |   
#            |                  |                       |                                 |                                                          |             |               |             |              |      \     | 
#            |                  |------------           |------------                     |                                                          |             |               |             |              |       \    |
#            |                  |                       |                                 |                                                          |             |               |             |              |        \   |
#            |                  |                       |                                 |                                            |             |             |               |             |              |         \  | 
#            |                  |                       |                                 |                                             \           /               \             /              |              |          \ |
#            |_ _ _ _ _ _ _     |_ _ _ _ _ _ _          |                                 |                                              \ _ _ _ _ /                 \ _ _ _ _ _ /             _ _ _            |           \|
                                                                                                                                                                                             










# maxx.execute(
#     "CREATE DATABASE leftpro"
# )
# print("Bajarildi🫡")

# maxx.execute(
#     """
#         CREATE TABLE odamlar(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR (100)
#         )
#     """
# )
# print("Tayyor")

# maxx.execute(
#     """
#         CREATE TABLE kasblar(
#         id SERIAL PRIMARY KEY,
#         title VARCHAR (100)
#         )
#     """
# )
# print("Tayyor")

# maxx.execute(
#     """
#     CREATE TABLE tenglarshtirish(   
#     odamlar_id INTEGER,
#     kasblar_id INTEGER
#     )
#     """
# )
# print("Tayyor")


# maxx.execute(
#     "INSERT INTO odamlar(name) VALUES('Aziz')"
# )
# print("Qo'shildi")

# maxx.execute(
#     "INSERT INTO kasblar(title) VALUES('UI-UX')"
# )
# print("Qo'shildi")


# maxx.execute( 
#      "SELECT * FROM kasblar"
# )
# rows = maxx.fetchall()
# for i in rows :
#     print(i)







