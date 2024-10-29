import streamlit as st


# === Functions ===


# === State ===


# === UI ===
st.title("Register")

task, project, milestone = st.tabs(["Tasks", "Projects", "Milestones"])

with task:
    st.selectbox(
        "Project",
        ["Project 1", "Project 2", "Project 3"],
        key="task_project"
    )
    st.selectbox(
        "Milestone",
        ["Milestone 1", "Milestone 2", "Milestone 3"],
        key="task_milestone"
    )
    st.selectbox(
        "Parent Task",
        ["Task 1", "Task 2", "Task 3"],
        key="task_parent"
    )

    st.text_input(
        "Title",
        key="task_title"
    )
    st.text_area(
        "Description",
        key="task_description"
    )

    st.date_input(
        "Due Date",
        key="task_due_date"
    )

    st.slider(
        "Importance",
        min_value=1,
        max_value=5,
        value=3,
        step=1,
        key="task_importance"
    )
    st.slider(
        "Urgency",
        min_value=1,
        max_value=5,
        value=3,
        step=1,
        key="task_urgency"
    )

    st.number_input(
        "Estimated Effort (hours)",
        min_value=0.5,
        step=0.5,
        value=4.0,
        key="task_effort"
    )

with project:
    st.text_input(
        "Name",
        key="project_name"
    )
    st.text_area(
        "Description",
        key="project_description"
    )

    st.selectbox(
        "Priority",
        ["Low", "Medium", "High"],
        key="project_priority"
    )

with milestone:
    st.text_input(
        "Name",
        key="milestone_name"
    )
    st.text_area(
        "Description",
        key="milestone_description"
    )

    st.date_input(
        "Due Date",
        key="milestone_due_date"
    )
