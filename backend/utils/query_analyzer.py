from utils.openai_connection import connect_open_ai

def analyze_query(query):
    openai = connect_open_ai()
    messages = [
        {"role": "system", "content": "You are an AI assistant. Classify the following query as either 'factual', 'statistical', or 'complex relationship'."},
        {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        n=1,
        temperature=0.7,
    )
    
    classification = response.choices[0].message.content.strip().lower()
    return classification
