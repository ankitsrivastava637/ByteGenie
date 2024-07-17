# ByteGenie Project

ByteGenie is an AI-powered chatbot application that converts natural language queries into SQL and retrieves relevant data from a database. This README provides instructions for setting up the project, including installing dependencies, configuring the database, loading data, and running the application.

## Table of Contents
- [Installation](#installation)
- [Setting Up the Database](#setting-up-the-database)
- [Loading Data into the Database](#loading-data-into-the-database)
- [Running the Application](#running-the-application)
- [Architecture](#architecture)

## Installation

### Clone the Repository

```sh
git clone https://github.com/ankitsrivastava637/ByteGenie.git
cd ByteGenie
```

### Backend Dependencies

Navigate to the `backend` directory and install the required Python packages:

```sh
cd backend
pip install -r requirements.txt
```

### Frontend Dependencies

Navigate to the `frontend` directory and install the npm packages:

```sh
cd ../frontend
npm install
```

## Setting Up the Database

### Configure Environment Variables

Create a `.env` file in the `backend` directory (if not already present) and configure your database connection details. You can use the provided `.env.sample` as a template:

```sh
cd ../backend
cp .env.sample .env
\```

Edit the `.env` file to include your specific database configuration:

```plaintext
DB_SERVER=sqlite:///./test.db
DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=
DB_PORT=
OPENAI_KEY=your_openai_api_key
```

### Create Database Schema

Create the database schema using the `create_schema.py` script:

```sh
python scripts/create_schema.py
```

## Loading Data into the Database

Run the data loading and preprocessing script to populate your database:

```sh
python scripts/load_data_from_csv.py
```

## Running the Application

### Start the Backend Server

Start the FastAPI server:

```sh
uvicorn app:app --reload
```

### Start the Frontend Application

Navigate to the `frontend` directory and start the React application:

\```sh
cd ../frontend
npm run dev
\```

## Notes on how our RAG works for text to sql 

The inspiration for such arhictecture has been taken from https://blog.futuresmart.ai/mastering-natural-language-to-sql-with-langchain-nl2sql#heading-implementing-memory-in-your-nl2sql-model

The architecture contains several key steps and optimizations that made the process efficient:

1. **Few-shot Examples**: Added more few-shot examples to improve the accuracy of the SQL query generation.
2. **Dynamic Few-shot Example Selection**: Implemented dynamic selection of the most relevant few-shot examples based on the query.
3. **Dynamic Relevant Table Selection**: Enhanced the selection of relevant tables by generating and using table descriptions during data loading.
4. **Customizing Prompts**: Improved the customization of prompts to better handle various types of queries.
5. **Adding Memory to the Chatbot**: Integrated a memory module to enable the chatbot to handle follow-up questions related to the database context.


## Benefits of this arhcitecture :

1. These steps enhanced the overall performance and accuracy of the AI-powered SQL query generation, making the chatbot more effective and efficient. 
2. It also takes care that if there are high number of tables in the database. 
3. The prompt is optimized select only relevant table and schema for question answering. This thereby improves speed and reduces cost of calling LLM.
4. The project also includes query analyzer, which would eventually help in future to segment the different type of user query to be routed to existing RAG process or a new GraphRAG process(discussed later in this page) for handling all factual, statistical and complex relational graph based question in much better way.
   
## Future improvements to the chatbot :

1. Implement fine-tuning of the model to improve the accuracy of the query generation, once more data is available.
2. Implement a more efficient and effective way of selecting relevant few-shot examples.
3. Verify the email generated are valid.
4. Implement a more efficient and effective way of selecting relevant tables.
5. Implement a more efficient and effective way of generating table descriptions.
6. Incorporate a more efficient and effective way of handling follow-up questions.
7. Incorporate vector database storage to improve the performance of the chatbot and make it more private.
8. Incorprate GraphRag introduced recently by microsoft to handle more complex relationship graphs based queries. GraphRag is a graph-based model that can handle queries that involve multiple tables and multiple relationships between them. More on it can be found on this https://microsoft.github.io/graphrag/

## Architecture DIAGRAMS :

The following diagrams illustrates the overall architecture of the AI chatbot, including both backend and frontend components, as well as the Retrieval-Augmented Generation (RAG) architecture:


### Overall Architecture : 

![diagram (2)](https://github.com/user-attachments/assets/f8b22c7f-9860-4d60-b196-2d675d5958d9)

### RAG architecture : 

![diagram (1)](https://github.com/user-attachments/assets/7b14bece-3795-476e-b065-98818f0c0b08)


- **Backend**:
  - **FastAPI Server**: Handles API requests.
  - **SQLite Database**: Stores the data.
  - **SQLAlchemy ORM**: Manages database interactions.
  - **LangChain**: Processes natural language queries.
  - **OpenAI API**: Generates SQL queries from natural language.
  - **Data Preprocessing Scripts**: Loads and preprocesses data.
  - **RAG Retriever**: Retrieves relevant documents to augment query generation.
  - **Query Analyzer**: Analyzes and categorizes queries (factual, statistical, complex).
  - **Memory Module**: Maintains conversation history for context-aware responses.

- **Frontend**:
  - **React Application**: User interface for interacting with the chatbot.
  - **Axios API Calls**: Manages communication between the frontend and backend.

