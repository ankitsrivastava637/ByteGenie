import pandas as pd
from langchain.llms import OpenAI
import json
from utils.standardize_data import convert_revenue_to_numeric, generate_email, standardize_employees, standardize_industry

def generate_table_description(table_name, table_data):
    llm = OpenAI(model_name="gpt-3.5-turbo-16k-0613", temperature=0)
    description_prompt = f"Generate a detailed description for the table {table_name} with columns: {', '.join(table_data.columns)}"
    description = llm(description_prompt)
    return description

def load_and_preprocess_data():
    people_df = pd.read_csv('backend/content/people_info.csv')
    event_df = pd.read_csv('backend/content/event_info.csv')
    company_df = pd.read_csv('backend/content/company_info.csv')

    # Standardize data
    company_df['company_revenue'] = company_df.apply(lambda row: convert_revenue_to_numeric(row['company_revenue']), axis=1)
    people_df['email'] = people_df.apply(lambda row: generate_email(row), axis=1)
    company_df['n_employees'] = company_df.apply(lambda row: standardize_employees(row['n_employees']), axis=1)
    company_df['company_industry'] = company_df.apply(lambda row: standardize_industry(row['company_industry']), axis=1)

    # Merge dataframes
    events_companies = event_df.merge(company_df, left_on='event_url', right_on='homepage_base_url', how='left')
    full_data = events_companies.merge(people_df, left_on='homepage_base_url', right_on='homepage_base_url', how='left')

    # Generate table descriptions
    table_descriptions = {
        "people": generate_table_description("people", people_df),
        "events": generate_table_description("events", event_df),
        "companies": generate_table_description("companies", company_df)
    }

    full_data['table_description'] = "Combined data for events, companies, and people."

    # Save processed data and descriptions
    full_data.to_csv('backend/content/processed_data.csv', index=False)
    with open('backend/content/table_descriptions.json', 'w') as f:
        json.dump(table_descriptions, f)

    return full_data, table_descriptions

# Execute the function to load and preprocess data
data, table_descriptions = load_and_preprocess_data()
