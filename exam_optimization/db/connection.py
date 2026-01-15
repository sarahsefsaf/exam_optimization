import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="exam_optimization",
        user="postgres",
        password="hana1234",
        host="localhost",
        port="5432"
    )