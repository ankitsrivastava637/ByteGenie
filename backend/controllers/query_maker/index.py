from fastapi import APIRouter, Request
from utils.custom_prompt import generate_sql_with_custom_prompt
import pandas as pd
from config.index import db

router = APIRouter()

@router.post("/query")
async def handle_query(request: Request):
    data = await request.json()
    natural_query = data['query']
    sql_query = generate_sql_with_custom_prompt(natural_query)
    # Execute the SQL query and return results
    result = pd.read_sql_query(sql_query, db.engine)
    return {"result": result.to_dict(orient="records")}
