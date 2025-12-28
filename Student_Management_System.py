import sqlite3

conn = sqlite3.connect("college.db")
conn.execute("PRAGMA foreign_keys = ON") # Wake up security guard!
cursor = conn.cursor()

# --- STEP 1: RESET & CREATE TABLES ---
cursor.execute("DROP TABLE IF EXISTS enrollments")
cursor.execute("DROP TABLE IF EXISTS courses")
cursor.execute("DROP TABLE IF EXISTS students")

# Table 1: Students
cursor.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
)
""")

# Table 2: Courses
cursor.execute("""
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    fees INTEGER
)
""")

# Table 3: Enrollments (The Link)
# This table maps Student ID -> Course ID
cursor.execute("""
CREATE TABLE enrollments (
    enroll_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")

# --- STEP 2: ADD DATA ---
print("--- Adding Data ---")
# Add Students
cursor.execute("INSERT INTO students VALUES (1, 'Harsh', 'harsh@gmail.com')")
cursor.execute("INSERT INTO students VALUES (2, 'Ram', 'ram@yahoo.com')")

# Add Courses
cursor.execute("INSERT INTO courses VALUES (101, 'Python Masterclass', 5000)")
cursor.execute("INSERT INTO courses VALUES (102, 'Data Science', 8000)")

# Add Enrollments (Linking them!)
# Harsh (1) takes Python (101)
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (1, 101)")
# Harsh (1) ALSO takes Data Science (102)
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (1, 102)")
# Ram (2) takes Python (101)
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (2, 101)")

conn.commit()

# --- STEP 3: GENERATE REPORTS (The Result) ---

print("\n--- 1. ENROLLMENT LIST  ---\n")
# We need to JOIN 3 Tables: Students -> Enrollments -> Courses
sql_list = """
SELECT students.name, courses.title, courses.fees
FROM enrollments
JOIN students ON enrollments.student_id = students.student_id
JOIN courses ON enrollments.course_id = courses.course_id
"""
for row in conn.execute(sql_list):
    print(f"Student: {row[0]:<10} | Course: {row[1]:<20} | Fees: ₹{row[2]}")

print("\n--- 2. REVENUE REPORT ---\n")
# Calculate Total Fees collected
cursor.execute("""
SELECT SUM(courses.fees) 
FROM enrollments 
JOIN courses ON enrollments.course_id = courses.course_id
""")

total_revenue = cursor.fetchone()[0]
print(f"TOTAL COLLEGE REVENUE: ₹{total_revenue}")

conn.close()