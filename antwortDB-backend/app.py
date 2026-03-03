import streamlit as st
import requests

st.set_page_config(page_title="antwortDB")

st.title("🧠 antwortDB — DB Assistant")

API_URL = "http://127.0.0.1:8000/query"


# -----------------------
# Chat Memory
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


question = st.chat_input("Ask your database")

if question:

    # show user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    # -----------------------
    # CALL REST API
    # -----------------------
    with st.spinner("Thinking..."):

        response = requests.post(
            API_URL,
            json={"question": question},
            timeout=120
        )

        result = response.json()

    sql = result["sql"]
    data = result["data"]

    # -----------------------
    # Display result
    # -----------------------
    with st.chat_message("assistant"):

        st.markdown("### Generated SQL")
        st.code(sql, language="sql")

        st.markdown("### Result")
        st.dataframe(data)

    st.session_state.messages.append(
        {"role": "assistant", "content": sql}
    )
