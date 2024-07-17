from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.query_maker import handle_query as query_maker_router
from scripts.load_data_from_csv import load_and_preprocess_data

# Load data and table descriptions at startup
data, table_descriptions = load_and_preprocess_data()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_maker_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
