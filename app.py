# ======================================
# OpenClaw Streamlit UI
# 主控层（Orchestrator）
# ======================================

import streamlit as st

# ======================================
# Agents
# ======================================

from agents.autonomous_teacher import (
    autonomous_task
)

# ======================================
# LLM
# ======================================

from llm.llm_client import ask_llm

# ======================================
# Systems
# ======================================

from systems.memory_system import (
    update_memory,
    load_memory
)

from systems.reflection_system import (
    reflect,
    load_reflection
)

from systems.evaluation_system import (
    evaluate_result
)

from systems.trace_system import (
    log_trace
)

from systems.experience_system import (
    summarize_experience,
    load_experience
)

from systems.log_system import (
    log_task,
    load_logs
)

# ======================================
# Tools
# ======================================

from tools.news_tools import (
    search_web,
    read_webpage,
    summarize_chunks,
    search_and_read
)

from tools.system_tools import (
    open_browser,
    open_notepad,
    create_file,
    list_files,
    write_code,
    run_python
)

from tools.excel_tools import (
    analyze_excel
)

# ======================================
# Streamlit UI
# ======================================

st.set_page_config(
    page_title="OpenClaw Assistant",
    layout="wide"
)

st.title("🤖 OpenClaw Autonomous Agent")

# ======================================
# Session
# ======================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

# ======================================
# Agent Planning
# ======================================

def plan_task(user_input):

    memory = load_memory()

    prompt = f"""
你是一个会自我优化的AI Agent。

用户长期记忆：
{memory}

历史经验：
{load_experience()}

历史反思：
{load_reflection()}

请注意：
- 避免重复错误
- 优先使用成功策略
- 提高效率

工具：
- search_web
- read_web
- summarize
- open_browser
- open_notepad
- create_file
- write_code
- run_python
- search_and_read

输出格式：

STEP1: ...
STEP2: ...

任务：
{user_input}
"""

    return ask_llm(prompt)

# ======================================
# Tool Registry
# ======================================

TOOLS = {

    "open_notepad": open_notepad,
    "open_browser": open_browser,
    "list_files": list_files,

}

# ======================================
# Execute Step
# ======================================

def execute_step(step):

    try:

        step_lower = step.lower()

        # ===== Simple Tools =====

        for tool_name, tool_func in TOOLS.items():

            if tool_name in step_lower:
                return tool_func()

        # ===== create_file =====

        if "create_file" in step_lower:

            parts = step.split()

            if len(parts) >= 2:
                return create_file(parts[-1])

        # ===== write_code =====

        if "write_code" in step_lower:
            return write_code(
                "generated.py",
                "print('hello from AI')"
            )

        # ===== run_python =====

        if "run_python" in step_lower:
            return run_python("generated.py")

        # ===== search_web =====

        if "search_web" in step_lower:

            query = (
                step_lower
                .replace("search_web", "")
                .strip()
            )

            return search_web(query)

        # ===== read_web =====

        if "read_web" in step_lower:

            url = step.split()[-1]

            chunks = read_webpage(url)

            return summarize_chunks(chunks)

        # ===== search_and_read =====

        if "search_and_read" in step_lower:

            query = (
                step_lower
                .replace("search_and_read", "")
                .strip()
            )

            return search_and_read(query)

    except Exception as e:

        return f"失败: {e}"

    return "无法执行该步骤"

# ======================================
# Chat Display
# ======================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ======================================
# File Upload
# ======================================

uploaded_file = st.file_uploader(
    "上传Excel文件",
    type=["xlsx"]
)

if uploaded_file:

    result = analyze_excel(uploaded_file)

    st.session_state.messages.append({
        "role": "assistant",
        "content": result
    })

# ======================================
# User Input
# ======================================

user_input = st.text_input(
    "请输入你的指令："
)

# ======================================
# Execute Button
# ======================================

if st.button("执行"):

    if user_input:

        # ===== Update Memory =====

        update_memory(user_input)

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # ======================================
        # Simple Rule-Based Commands
        # ======================================

        if "记事本" in user_input:

            result = open_notepad()

            st.session_state.history.append(
                (user_input, result)
            )

        elif "浏览器" in user_input:

            result = open_browser()

            st.session_state.history.append(
                (user_input, result)
            )

        # ======================================
        # Complex Agent Tasks
        # ======================================

        else:

            plan = plan_task(user_input)

            status_box = st.empty()

            results = []

            steps = plan.split("\n")

            max_retry = 2

            for step in steps:

                if "STEP" in step:

                    retry = 0

                    success = False

                    while retry < max_retry and not success:

                        status_box.markdown(
                            f"🧠 执行: {step} "
                            f"(尝试 {retry+1})"
                        )

                        result = execute_step(step)

                        log_trace(step, result)

                        # ======================================
                        # Failure Detection
                        # ======================================

                        if (
                            result is None
                            or "失败" in str(result)
                            or "无法执行" in str(result)
                        ):

                            retry += 1

                            fix_prompt = f"""
                                原步骤执行失败：

                                {step}

                                错误：

                                {result}

                                请修复这个步骤。

                                只返回 STEP 格式。
                                """

                            step = ask_llm(fix_prompt)

                        else:

                            success = True

                            results.append(
                                f"✅ {step} → {result}"
                            )

                            status_box.markdown(
                                f"✅ 完成: {step}"
                            )

                    if not success:

                        results.append(
                            f"❌ 最终失败: {step}"
                        )

            # ======================================
            # Final Result
            # ======================================

            final_result = (
                f"🧠 任务计划:\n{plan}\n\n"
                f"⚙️ 执行结果:\n"
                + "\n".join(results)
            )

            # ======================================
            # Learning Systems
            # ======================================

            log_task(user_input, final_result)

            summarize_experience(
                user_input,
                final_result
            )

            reflection = reflect(
                user_input,
                final_result
            )

            score = evaluate_result(
                user_input,
                final_result
            )

            st.write("📊 评分:", score)

            # ======================================
            # Save History
            # ======================================

            st.session_state.history.append(
                (user_input, final_result)
            )

            st.rerun()

# ======================================
# Conversation History
# ======================================

for q, a in reversed(
    st.session_state.history
):

    st.markdown(f"**你:** {q}")

    st.markdown(f"**AI:** {a}")

    st.markdown("---")