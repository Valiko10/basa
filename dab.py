import psycopg2
import django

# ulash = psycopg2.connect(
#     host='localhost',
#     database = 'it_park',
#     user = 'postgres',
#     password = 'yangiobod84'
# )
# ulash.autocommit =True
# ishlatish = ulash.cursor()

# ishlatish.execute(
#     "INSERT INTO talabalar (name , age) VALUES ('4-Ulugbek' , 132)"
# )
# ulash.commit()

# ustunlar = ishlatish.fetchall()
# for ustun in ustunlar:
#     print(ustun)


# ishlatish.execute(
#     "SELECT * FROM talabalar"
# )
# ulash.commit()



# ishlatish.execute(
#     # "UPDATE talabalar SET  name = 'Quloq' WHERE name = 'Yoqubboy'"
#                         #              |
#                         #  yoqubboyi quloqa o'zgartiradi
#     # "UPDATE talabalar SET  name = '' WHERE name = 'Yoqubboy'"
#     "UPDATE talabalar SET age = age + 123463"
# )
# ulash.commit()


# ishlatish.execute(
#     "SELECT * FROM talabalar "
# )
# rows = ishlatish.fetchall()

# for row in rows:
#     print(row)







ulash = psycopg2.connect(
    host = 'localhost',
    database = 'axv',
    user = 'postgres',
    password = 'yangiobod84',

)
ulash.autocommit = True
connect = ulash.cursor()

# connect.execute(
#     "CREATE DATABASE axv"
# )
# print("bajarildi")

# Teachers
# connect.execute(
#     """
#     CREATE TABLE teachers(
#       id SERIAL PRIMARY KEY,
#       name VARCHAR(101),
#       tajriba_yili INTEGER ,
#       subject VARCHAR(101)
#     )
#     """
# )
# print("Teachers qabul qilindi")

# Students
# connect.execute(
#     """
#     CREATE TABLE student(
#       id SERIAL PRIMARY KEY,
#       name VARCHAR(101),
#       age INTEGER ,
#       subject VARCHAR(101)
#     )
#     """
# )
# print("Ajoyib")

# N1
# connect.execute(
#     "INSERT INTO student (name,age,subject) VALUES ('Valijon',15,'Fullsteak')"
# )
# print("Chotki yuklandi 👌")

# N2
# connect.execute(
#     "INSERT INTO student(name,age,subject) VALUES ('Ulugbek',15,'AI')"
# )
# print("Chotki yuklandi 👌")

# N3
# connect.execute(
#     "INSERT INTO student (name,age,subject) VALUES ('Yoqubboy',15,'Back-end')"
# )
# print("Chotki yuklandi 👌")


# N4
# connect.execute(
#     "INSERT INTO student(name,age,subject) VALUES ('Hurumdor',15,'telegram bot')"
# )
# print("Chotki yuklandi 👌")


# N5
# connect.execute(
#     "INSERT INTO student (name,age,subject) VALUES ('Yoqubboy',15,'Back-end')"
# )
# print("Chotki yuklandi 👌")

# N6
# connect.execute(
#     "INSERT INTO student(name,age,subject) VALUES ('Hurumdor',15,'telegram bot')"
# )
# print("Chotki yuklandi 👌")



# Student run

# connect.execute(
#     "SELECT * FROM student "
# )
# chop_etamiz = connect.fetchall()
# for sikl_bilan_chop_etamiz in chop_etamiz:
#     print(sikl_bilan_chop_etamiz)

# connect.execute(
#     "INSERT INTO teachers(name,tajriba_yili,subject) VALUES ('Mirzabek',5,'Fullset')"
# )
# print("Chotki yuklandi 👌")



# N2
# connect.execute(
#     "INSERT INTO teachers(name,tajriba_yili,subject) VALUES ('Kamoliddin',3,'Back-end')"
# )
# print("Chotki yuklandi 👌")

# connect.execute(
#     "INSERT INTO teachers(name,tajriba_yili,subject) VALUES ('Azamat',6,'UI-UX')"
# )
# print("Chotki yuklandi 👌")


# connect.execute(
#     "INSERT INTO teachers(name,tajriba_yili,subject) VALUES ('Nodirbek',4,'Telegram Bot')"
# )
# print("Chotki yuklandi 👌")



connect.execute(
    "SELECT * FROM teachers "
)

chop_etamiz = connect.fetchall()
for sikl_bilan_chop_etamiz in chop_etamiz:
    print(sikl_bilan_chop_etamiz)

ulash.commit()