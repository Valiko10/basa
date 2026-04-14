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
#     "CREATE DATABASE patients"
# )
# print("👌")

# cur.execute(
#     """
#     CREATE TABLE patient(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("👌")

# cur.execute(
#     """
#     CREATE TABLE doctors(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100)
#     )
#     """
# )
# print("👌")

# cur.execute(
#     """
#     CREATE TABLE cilinic(   
#     patient_id INTEGER,
#     doctors_id INTEGER
#     )

#     """
# )
# cur.execute(
#     "INSERT INTO patient(name)  VALUES('Munis')"
# )
# print("👌")

# doctors

# cur.execute(
#     "INSERT INTO doctors(name)  VALUES('Rustam')"
# )
# print("👌")

# sinov

# cur.execute(
#     "SELECT * FROM doctors"
# )
# # print('🙌')

# rows = cur.fetchall()
# for row in rows:
#     print(row)


# finish Join

# cur.execute(
#     "INSERT INTO cilinic(patient_id,doctors_id) VALUES(2,2)"
# )
# print("👌")



# cur.execute(
#     "SELECT patient.name , doctors.name FROM cilinic JOIN patient ON patient.id = cilinic.patient_id JOIN doctors ON doctors.id = cilinic.doctors_id "
# )
# rows = cur.fetchall()
# # print(rows)
# for row in rows:
#     print(row)



# cur.execute(
#     "SELECT * FROM cilinic"
# )
# cur.execute(
#     "SELECT * FROM doctors"
# )
# cur.execute(
#     "SELECT * FROM patient"
# )
# print('🙌')
# for row in rows:
#     print(row)
# cur.execute(
#     "INSERT INTO clinic(patient_id,doctors_id) VALUES(3,3)"
# )


