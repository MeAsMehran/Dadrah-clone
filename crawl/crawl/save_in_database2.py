from datetime import datetime

import os
import django
import json


# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dadrah.settings')
django.setup()

from crawl_scrape.models import Answer, Question



with open("spiders/questionData2.json", "r", encoding="utf-8") as file:
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


print("Data Saved in Database Successfully!")