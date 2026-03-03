from core.semantic_model import SEMANTIC_MODEL


def build_prompt(question, schema):

    schema_text = "\n".join(
        f"{t}: {cols}" for t, cols in schema.items()
    )

    semantic_text = ""

    for table, meta in SEMANTIC_MODEL.items():

        semantic_text += f"""
Table: {table}
Role: {meta['role']}
Grain: {meta.get('grain','')}
Measures: {meta.get('measures',[])}
"""

    prompt = (
        "You are antwortDB, an analytics SQL assistant.\n\n"

        "DATABASE TYPE: SQLite\n\n"

        "RULES:\n"
        "- Use ONLY listed tables\n"
        "- Aggregations must use FACT table measures\n"
        "- DIMENSION tables are for grouping\n"
        "- Avoid multiplying measures across tables\n"
        "- Prefer SUM(price) for revenue-style questions\n"
        "- Return SQL inside ```sql``` block\n\n"

        "DATABASE SCHEMA:\n"
        f"{schema_text}\n\n"

        "SEMANTIC MODEL:\n"
        f"{semantic_text}\n\n"

        "QUESTION:\n"
        f"{question}\n"
    )

    return prompt