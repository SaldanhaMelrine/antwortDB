from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.llm_service import generate_sql
from backend.services.db_service import run_query

router = APIRouter()


class Query(BaseModel):
    question: str


@router.post("/query")
def query(q: Query):

    sql = generate_sql(q.question)
    data = run_query(sql)

    return {
        "sql": sql,
        "data": data
    }
