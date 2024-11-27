from datetime import datetime

import os
import django

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dadrah.settings')
django.setup()

import psycopg2
from Dadrah.settings import DATABASES

from crawl_scrape.models import Answer, Question

my_db = DATABASES['crawler_db']
print(my_db, "\n")

# connection
# conn = psycopg2.connect(database="your_database_name",
#                     user="postgres",
#                     password="admin",
#                     host="localhost",  # or your database server's address
#                     port="5432"        # default PostgreSQL port
#                     )

conn = psycopg2.connect(database=my_db['NAME'],
                        user=my_db['USER'],
                        password=my_db['PASSWORD'],
                        host=my_db['HOST'],
                        port=my_db['PORT'])

# cursor
cur = conn.cursor()
print("PostgreSQL database connected!")

# CREATING THE QUESTION TABLE (WE SHOULD CREATE ANY TABLE ONCE AND THEN COMMENT IT!!!!) AND THEN commit the changes to database
# cur.execute("""CREATE TABLE question (
#                 id SERIAL PRIMARY KEY ,
#                 question_title VARCHAR(64),
#                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#                 question_text TEXT,
#                 question_url VARCHAR(64))""")
#
# conn.commit()


# CREATING THE ANSWER TABLE (WE SHOULD CREATE ANY TABLE ONCE AND THEN COMMENT IT!!!!) AND THEN commit the changes to database
# cur.execute("""CREATE TABLE answer (
#                 id SERIAL PRIMARY KEY ,
#                 answer_content TEXT,
#                 answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#                 answer_lawyer VARCHAR(64),
#                 answer_rate NUMERIC)""")
#
# conn.commit()


# created_at = datetime.now()
# print(created_at)

####################### WAY 1 INSERTING ITEM #######################
# WAY 1: TO INSERT A ITEM TO DATABASE (WE SHOULD COMMIT IT)
# cur.execute("""
# INSERT INTO question (question_title, created_at, question_text, question_url)
# VALUES (%s, %s, %s, %s);
# """, ('hellloooo', created_at, 'dsafasdfasfaf mememmememememememme', 'question/12'))
# conn.commit()


####################### WAY 2 INSERTING ITEM #######################
# WAY 2: TO INSERT A ITEM TO DATABASE
# cur.execute("""
# INSERT INTO question (question_title, created_at, question_text, question_url)
# VALUES ('hellloooo2', '2024-11-20 13:28:22.185218', 'dsafasdfasfaf mememmememememememme2', 'question/15');
# """, )
# conn.commit()
#
#
# cur.execute("""SELECT * FROM question""")
# result = cur.fetchall()
# print(result)


# this code will create a table and check if it exists in database or not
# try:
#     # Execute the SQL command
#     cur.execute("""
#         CREATE TABLE hello (
#             id SERIAL PRIMARY KEY,
#             username VARCHAR(50) NOT NULL,
#             email VARCHAR(100) UNIQUE NOT NULL,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         );
#     """)
#     # Commit the transaction
#     conn.commit()
#     print("Table created successfully!")
# except Exception as e:
#     print("Error occurred:", e)
#     conn.rollback()  # Roll back the transaction if something goes wrong
# finally:
#     # Close the connection
#     cur.close()
#     conn.close()


import json

with open("questionData2.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)
# print(data)

for item in data:
    question = item.get("question", {})
    answers = item.get("answers", {})

    # print("Title:", question.get("question_title", "N/A"))
    question_title = question.get("question_title", "N/A")

    # print("Date:", question.get("question_date", "N/A"))
    created_at = question.get("question_date", "N/A")

    # print("Text:", question.get("question_text", "N/A"))
    question_text = question.get("question_text", "N/A")

    # print("URL:", question.get("question_url", "N/A"))
    question_url = question.get("question_url", "N/A")

    q = Question.objects.create(question_title=question_title, created_at=created_at, question_text=question_text,
                                question_url=question_url)
    # print("---------")

    # GIVES ALL THE ANSWERS DETAILS
    for answer in answers:
        # print("Content: ", answer.get("answer_content", ))
        answer_content = answer.get("answer_content", )

        # print("Date: ", answer.get("answer_date", ))
        created_at = answer.get("answer_date", )

        # print("Lawyer: ", answer.get("answer_lawyer", ))
        answer_lawyer = answer.get("answer_lawyer", )

        # print("Rate: ", answer.get("answer_rating", ))
        answer_rate = float(answer.get("answer_rating", ).replace("Rate: ", ""))

        a = Answer.objects.create(answer_content=answer_content, created_at=created_at, answer_lawyer=answer_lawyer,
                                  answer_rate=answer_rate, question_id=q)

        # print("-" * 40)

    # print('#' * 40)

# with open("newFile.json", "w", encoding="utf-8") as new_file:
#     questions = []
#     for item in data:
#         question = item.get("question", {})
#         questions.append(question)
#
#     json.dump(questions, new_file, indent=2)


####################### WAY 2 INSERTING ITEM #######################
# WAY 2: TO INSERT A ITEM TO DATABASE
# cur.execute("""
# INSERT INTO question (question_title, created_at, question_text, question_url)
# VALUES ('hellloooo2', '2024-11-20 13:28:22.185218', 'dsafasdfasfaf mememmememememememme2', 'question/15');
# """, )
# conn.commit()
