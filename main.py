from datetime import datetime
from faker import Faker
import random
import sqlite3

fake = Faker('uk_UA')

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date_received DATE)''')

groups = ['Group 1', 'Group 2', 'Group 3']
for group_name in groups:
    cursor.execute('''INSERT INTO groups (name) VALUES (?)''', (group_name,))

teachers = [fake.name() for _ in range(5)]
for teacher_name in teachers:
    cursor.execute('''INSERT INTO teachers (name) VALUES (?)''', (teacher_name,))

subjects = ['Mathematics', 'Physics', 'Chemistry', 'History', 'Literature', 'Computer Science', 'Biology', 'Geography']
for subject_name in subjects:
    teacher_id = random.randint(1, 5)
    cursor.execute('''INSERT INTO subjects (name, teacher_id) VALUES (?, ?)''', (subject_name, teacher_id))

for _ in range(40):
    student_name = fake.name()
    group_id = random.randint(1, 3)
    cursor.execute('''INSERT INTO students (name, group_id) VALUES (?, ?)''', (student_name, group_id))

for student_id in range(1, 41):
    for subject_id in range(1, 9):
        grade = random.randint(1, 100)
        date_received = datetime.now().date()
        cursor.execute('''INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)''',
                       (student_id, subject_id, grade, date_received))

conn.commit()

conn.close()
