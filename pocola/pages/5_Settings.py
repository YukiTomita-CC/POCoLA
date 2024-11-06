import streamlit as st


# === Functions ===


# === State ===


# === UI ===
st.title("Settings")

# 画面高さ基準
st.number_input(
    "Screen height base",
    min_value=0,
    max_value=1000,
    value=200,
    step=10,
    key="screen_height",
    )

# 1日の作業時間
st.number_input(
    "Hours per day",
    min_value=0,
    max_value=24,
    value=4,
    step=1,
    key="hours_per_day",
    )

# 具体的な〆切が無いタスクのデフォルトの〆切日(例: 30日後)
st.number_input(
    "Default deadline for tasks without specific deadlines",
    min_value=0,
    max_value=365,
    value=30,
    step=1,
    key="default_deadline",
    )

# タスクのバッファ時間(何倍か)
st.number_input(
    "Task buffer time (multiplier)",
    min_value=0.0,
    max_value=2.0,
    value=1.2,
    step=0.1,
    key="task_buffer_time",
    )

# タスクはforwardsかbackwardsどちらで詰めるか
# TODO: backwardsの実装
st.radio(
    "Task scheduling direction",
    options=["Forwards", "Backwards"],
    key="task_scheduling_direction",
    horizontal=True,
    )

# 同じimportanceのタスクの順序を難易度順にするか、得意なこと順にするか、すぐに終わる順にするか
st.radio(
    "Task order within the same importance",
    options=["Difficulty", "Skill", "Time to finish"],
    key="task_order_within_importance",
    horizontal=True,
    )

# その中で昇順か降順か
st.radio(
    "Task order within the same importance",
    options=["Ascending", "Descending"],
    key="task_order_within_importance_order",
    horizontal=True,
    )

# その日のタスクはプロジェクトでまとめるか、タスクのジャンルでまとめるか
st.radio(
    "Task grouping",
    options=["Project", "Genre"],
    key="task_grouping",
    horizontal=True,
    )

if st.button("Save"):
    pass
