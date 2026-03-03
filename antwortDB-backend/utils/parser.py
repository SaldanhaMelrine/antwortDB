import re


def extract_sql(response: str):

    if not response:
        raise ValueError("Empty LLM response")

    text = response.strip()

    # sql markdown block
    block = re.search(
        r"```sql(.*?)```",
        text,
        re.S | re.I
    )

    if block:
        return block.group(1).strip()

    # fallback
    guess = re.search(
        r"(SELECT|WITH).*",
        text,
        re.S | re.I
    )

    if guess:
        return guess.group(0).strip()

    raise ValueError(
        f"SQL not found:\n{text}"
    )
