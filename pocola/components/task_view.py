import streamlit as st


def convert_to_one_task_view(title, project, due_date):
    with st.container(height=200, border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(title)

        with col2:
            st.toggle(
                "Completed",
                key=f"completed_{title}"
                )

        st.write(f"Project: {project}")
        st.write(f"Due Date: {due_date}")
        st.write("Description: This is a test task.")
