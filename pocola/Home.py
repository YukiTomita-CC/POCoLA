import streamlit as st

from components.task_view import convert_to_one_task_view


st.set_page_config(layout="wide")
image_size = 3.5 # default=2
image_message_gap = 0.5 # default=0.5
CHAT_MESSAGE_STYLE = f"""<style>
img.eeusbqq0 {{
    width: {image_size}rem !important;
    height: {image_size}rem !important;
}}

.stChatMessage.eeusbqq4 {{
    gap: {image_message_gap}rem !important;
}}
</style>
"""
HEIGHT_STANDARD = 300

# === Functions ===


# === State ===


# === UI ===
st.title("POCoLA")
st.markdown(CHAT_MESSAGE_STYLE, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container(height=HEIGHT_STANDARD*2 + 15, border=True):
        st.subheader("Today's Tasks")

        convert_to_one_task_view("Task 1", "Project 1", "2022-01-01")
        convert_to_one_task_view("Task 2", "Project 2", "2022-01-02")
        convert_to_one_task_view("Task 3", "Project 3", "2022-01-03")

with col2:
    with st.container(height=HEIGHT_STANDARD, border=True):
        st.subheader("Assistant Messages")
        with st.chat_message("assistant"):
            st.write("Hello! How can I help you today?")

    with st.container(height=HEIGHT_STANDARD, border=True):
        st.subheader("Conditions")

        st.write("Very hot today!")
