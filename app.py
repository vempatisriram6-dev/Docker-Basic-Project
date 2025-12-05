import psycopg2
import time


time.sleep(5)

try:
    conn = psycopg2.connect(
        host="my-postgres",
        database="mydb",
        user="user",
        password="pass"
    )
    print("Connected to the PostgreSQL!\n", flush=True)

    cursor = conn.cursor()

    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            student_no INTEGER,
            name VARCHAR(50),
            course VARCHAR(50),
            age INTEGER
        );
    """)
    conn.commit()

    
    cursor.execute("TRUNCATE TABLE students RESTART IDENTITY;")
    conn.commit()

    
    cursor.execute("""
        INSERT INTO students (student_no, name, course, age)
        VALUES (101, 'Sriram', 'DevOps', 22)
        RETURNING id;
    """)
    inserted_id = cursor.fetchone()[0]
    conn.commit()

    
    cursor.execute("SELECT * FROM students;")
    rows = cursor.fetchall()

    print(f"Inserted row ID: {inserted_id}\n", flush=True)
    print("All rows in table:\n", flush=True)

    
    print("+----+-------------+---------+---------+-----+", flush=True)
    print("| ID | Student No. | Name    | Course  | Age |", flush=True)
    print("+----+-------------+---------+---------+-----+", flush=True)
    
    
    for row in rows:
        print(f"| {row[0]:<2} | {row[1]:<11} | {row[2]:<7} | {row[3]:<7} | {row[4]:<3} |", flush=True)

    print("+----+-------------+---------+---------+-----+", flush=True)

    cursor.close()
    conn.close()

except Exception as e:
    print("Connection failed:", e, flush=True)
