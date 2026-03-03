from core.prompt_builder import build_prompt
from core.ollama_client import ask_ollama
from core.schema_loader import load_schema
from utils.parser import extract_sql


def generate_sql(question):

    schema = load_schema()

    prompt = build_prompt(question, schema)

    response = ask_ollama(prompt)

    sql = extract_sql(response)

    return sql