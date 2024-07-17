import pandas as pd
import re

def convert_revenue_to_numeric(revenue):
    if pd.isna(revenue):
        return None
    revenue = revenue.lower().replace(",", "").replace("usd", "")
    if "million" in revenue:
        return float(re.findall(r"\d+\.\d+|\d+", revenue)[0]) * 1e6
    if "billion" in revenue:
        return float(re.findall(r"\d+\.\d+|\d+", revenue)[0]) * 1e9
    return float(re.findall(r"\d+\.\d+|\d+", revenue)[0])

def generate_email(first_name, last_name, email_pattern, homepage_base_url):
    if pd.isna(first_name) or pd.isna(last_name) or pd.isna(email_pattern):
        return None

    first_name = first_name.lower()
    last_name = last_name.lower()
    first_initial = first_name[0]
    last_initial = last_name[0]
    pattern = email_pattern
    base_url = homepage_base_url

    email = (
        pattern.replace("[first_initial]", first_initial)
        .replace("[last_initial]", last_initial)
        .replace("[first]", first_name)
        .replace("[last]", last_name)
        .replace(".", "")
        + "@"
        + base_url
    )
    return email

def standardize_employees(n_employees):
    if pd.isna(n_employees):
        return None

    n_employees = str(n_employees).replace("+", "").replace(",", "").replace("employees", "")

    if "-" in n_employees:
        parts = [float(x) for x in n_employees.split("-")]
        return int(max(parts))
    return int(float(n_employees))

def standardize_industry(industry):
    if pd.isna(industry):
        return industry
    return re.sub(r"[^a-z\s]", "", industry.lower().strip())
