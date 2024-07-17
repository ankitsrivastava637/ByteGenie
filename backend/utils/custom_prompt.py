from langchain.prompts import PromptTemplate
from utils.dynamic_selection import select_few_shot_examples
from utils.table_selection import select_relevant_tables, table_descriptions
from utils.memory import add_to_memory, get_memory
from config.index import db
from utils.query_analyzer import analyze_query
from utils.text_to_sql import text_to_sql

template = """
Use the following few-shot examples to help you generate SQL queries:

{few_shot_examples}

Only consider the relevant tables based on the query:
{relevant_tables}

Conversation history:
{conversation_history}

Convert the following natural language query to an SQL query:
{query}
"""

prompt = PromptTemplate(template=template, input_variables=["few_shot_examples", "relevant_tables", "conversation_history", "query"])

def generate_sql_with_custom_prompt(natural_query):
    query_type = analyze_query(natural_query)
    
    if query_type == "complex relationship":
        return text_to_sql(natural_query)
    
    examples = select_few_shot_examples(natural_query)
    relevant_tables = select_relevant_tables(natural_query, table_descriptions)
    conversation_history = get_memory().get_conversation()
    prompt_text = prompt.format(few_shot_examples=examples, relevant_tables=relevant_tables, conversation_history=conversation_history, query=natural_query)
    response = db.run(prompt_text)
    add_to_memory(natural_query, response)
    return response
