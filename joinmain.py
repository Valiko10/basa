# from join import db_connect

# conn  = db_connect()
# cur = conn.cursor()
# conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE l"
# )
# print("Create database")
# cur.execute(
#     """
#     CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )

#     """
# )
# print("Create table")

# cur.execute(
#     """
#     CREATE TABLE courses(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100)
#     )

#     """
# )
# print("Create table")
# # kursga yozilganlar
# cur.execute(
#     """
#     CREATE TABLE enrolments(   
#     student_id INTEGER,
#     course_id INTEGER
#     )

#     """
# )
# print("Create table")

# cur.execute(
#     "INSERT INTO students(name) VALUES('Zoxira')"
# )
# print("Add student")


# cur.execute(
#     "INSERT INTO courses(title) VALUES('Komputer savodxonligi')"
# )
# print("Success")
# cur.execute(
#     "SELECT * FROM enrolments"
# )
# rows = cur.fetchall()
# print(rows)
# cur.execute(
#     "INSERT INTO enrolments(student_id,course_id) VALUES(2,2)"
# )


# cur.execute(
#     "SELECT students.name ,courses.title FROM enrolments JOIN students ON students.id =enrolments.student_id JOIN courses ON courses.id = enrolments.course_id "
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)






    