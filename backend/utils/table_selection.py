import json

def select_relevant_tables(query, table_descriptions):
    relevant_tables = []
    for table, description in table_descriptions.items():
        if any(word in query.lower() for word in description.lower().split()):
            relevant_tables.append(table)
    return relevant_tables if relevant_tables else ["events", "companies", "people"]

# Load table descriptions at startup
with open('backend/content/table_descriptions.json') as f:
    table_descriptions = json.load(f)
