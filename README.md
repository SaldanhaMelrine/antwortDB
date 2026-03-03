# antwortDB

**LLM-Powered Natural Language to SQL Assistant**

antwortDB is a modular, schema-aware system that enables users to query structured databases using natural language and receive generated SQL and executed results.

---

## Demo

![antwortDB Demo](<img width="915" height="642" alt="image" src="https://github.com/user-attachments/assets/71c7b4a0-e9db-433a-b3bf-af76acbedff6" />


---

## Overview

antwortDB converts natural language queries into validated SQL statements and executes them against a relational database.

The system is designed to:

- Generate deterministic SQL output  
- Reduce hallucinated table/column references  
- Safely execute structured queries  
- Separate UI, business logic, LLM inference, and data access  

---

## Architecture

User (Browser)  
↓  
Streamlit UI  
↓  
FastAPI Backend (REST API)  
↓  
LLM (Llama 3 via Ollama)  
↓  
SQLite Database  

### Design Principles

- Separation of concerns  
- Schema-aware prompt construction  
- Controlled SQL execution  
- Modular backend components  
- LLM provider abstraction  

---

## System Flow

1. User submits natural language question  
2. Backend loads database schema metadata  
3. Structured prompt is constructed with schema context  
4. LLM generates SQL  
5. SQL is parsed and validated  
6. Query is executed against database  
7. Results are returned as structured JSON  
8. Frontend displays SQL and results  

---

## Core Components

### Streamlit (Frontend)

- Collects user input  
- Sends requests to backend  
- Displays generated SQL and results  

### FastAPI (Backend)

Main endpoint:

POST /query

Responsibilities:

- Load schema metadata  
- Construct structured prompts  
- Call LLM  
- Parse SQL output  
- Validate SQL safety  
- Execute query  
- Return structured response  

---

### Backend Modules

**schema_loader.py**  
Extracts table names, columns, and types using SQLAlchemy and injects schema into prompts to reduce hallucination.

**prompt_builder.py**  
Enforces SQL-only output and structured instructions to improve determinism.

**ollama_client.py**  
Handles LLM interaction and supports configurable model parameters.

**parser.py**  
Extracts clean SQL from LLM responses.

**sql_executor.py**  
Executes validated SQL and returns results in JSON format.

---

## Safety & Reliability

- Schema injection to prevent fabricated tables  
- SQL-only output enforcement  
- Validation before execution  
- Optional blocking of destructive queries  
- REST-based stateless architecture  

---

## Example

User Query:

How many orders were delayed?

Generated SQL:

SELECT COUNT(*)
FROM olist_orders_dataset
WHERE order_delivered_customer_date > order_estimated_delivery_date;

Returned Result:

7827

---

## Tech Stack

- Python  
- FastAPI  
- Streamlit  
- Llama 3 (Ollama)  
- SQLAlchemy  
- SQLite  
- Pandas  

---

## Installation

### Clone Repository

git clone https://github.com/yourusername/antwortDB.git  
cd antwortDB  

### Install Dependencies

pip install -r requirements.txt  

### Start Backend

uvicorn main:app --reload  

### Start Frontend

streamlit run app.py  

---

## Future Improvements

- PostgreSQL support  
- Authentication & access control  
- Query logging and monitoring  
- Caching layer  
- Dockerized deployment  
- Multi-database support  

---

## Project Intent

antwortDB demonstrates how LLM systems can be integrated with structured databases using modular backend design, schema-aware prompt engineering, and controlled execution layers.
