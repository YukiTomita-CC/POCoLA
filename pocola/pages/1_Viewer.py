import json

import streamlit as st


# === Functions ===


# === State ===


# === UI ===
task, project, milestone = st.tabs(["Tasks", "Projects", "Milestones"])

def common_ui(tab_name):
    st.title(f"{tab_name.capitalize()} Viewer")

    with st.expander("Filter"):
        st.write("Filter tasks here")

    st.markdown("---")

    data = []
    with open(f"tests/fake_data/fake_{tab_name}.jsonl", 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line.strip()))

    st.dataframe(
        data,
        use_container_width=True,
        key=tab_name
    )

with task:
    common_ui("tasks")

with project:
    common_ui("projects")

with milestone:
    common_ui("milestones")
