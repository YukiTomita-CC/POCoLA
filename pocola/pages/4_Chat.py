import streamlit as st

from clients.openai_for_dev import OpenAIClient


# === Functions ===


# === State ===
if "messages" not in st.session_state:
    st.session_state.messages = []
if "client" not in st.session_state:
    st.session_state.client = OpenAIClient()


# === UI ===
st.title("Chat")

for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Message Assistant..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = st.session_state.client.generate_response(
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )
        response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": response})
