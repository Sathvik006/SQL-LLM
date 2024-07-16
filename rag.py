import requests

def get_prompt(user_query, user, db_output):
    prompt = f"""You are an intelligent assistant that can understand user queries and provide detailed, accurate responses. You are given a user's query and the context, which includes data retrieved from a database. Your task is to use the provided context to answer the user's query. If the user's query includes a general question that cannot be answered using the database context, you should use your general knowledge to provide a comprehensive answer.

Rules:
1. Understand the user's query and the provided context.
2. Use the context to generate a solid, well-defined response.
3. IMPORTANT:In the response do not mention the user in {user_query} instead mention the user in {user} field.
4. If the query includes a general question, use your general knowledge to answer it.
5. If the Context {db_output} is "RAG" as the output, or if the context is missing, use your general knowledge to answer the question.
6. Provide a clear and detailed response that addresses all parts of the user's query.

User query: {user_query}

Context (database output): 
{db_output}

Your response:"""
    return prompt

def query_model(payload):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate_response(user_query, user, db_output):
    prompt = get_prompt(user_query, user, db_output)
    payload = {"inputs": prompt}
    response = query_model(payload)
    # Extract the generated text from the response
    response_text = response[0]['generated_text'].strip()
    if "Your response:" in response_text:
        response_text = response_text.split("Your response:")[1].strip()
    return response_text


