from db import query_database
from query import classify_response
from rag import generate_response


db = 'transactions.db'
user = "Country head"
user_query = "What country has highest price"
sql_query = classify_response(user, user_query)
print(sql_query)
if "RAG" in sql_query:
    db_output = "RAG"
    answer = generate_response(user_query, user, db_output)
else:
    db_output = query_database(db, sql_query)
    answer = generate_response(user_query, user, db_output)
print(db_output)
print(answer)


