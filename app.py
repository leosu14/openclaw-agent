# ======================================
# OpenClaw + Streamlit UI（基于你的版本改造）
# 运行：streamlit run app.py
# ======================================

import streamlit as st
from langchain_ollama import OllamaLLM
import os
import subprocess
import pandas as pd
from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

import json

# ======================================
# Memory
# ======================================
MEMORY_FILE = "memory.json"
EXPERIENCE_FILE = "experience.txt"
REFLECTION_FILE = "reflection.txt"
TRACE_FILE = "trace.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

memory = load_memory()


# ===== 初始化 =====
llm = OllamaLLM(model="llama3")

st.set_page_config(page_title="OpenClaw Assistant", layout="wide")
st.title("🤖 OpenClaw 本地AI助手")




# ======================================
# 自动任务系统（Daily Agent）
# ======================================

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

TASKS_FILE = "scheduled_tasks.json"
REPORT_FILE = "daily_report.txt"

scheduler = BackgroundScheduler()
scheduler.start()

# ======================================
# 自动任务日志
# ======================================

def save_report(task, result, reflection=""):
    with open(REPORT_FILE, "a", encoding="utf-8") as f:
        f.write(f"
===== {datetime.now()} =====
")
        f.write(f"任务: {task}
")
        f.write(f"结果:
{result}
")
        f.write(f"反思:
{reflection}
")

# ======================================
# 自动任务执行
# ======================================

def autonomous_task(task):

    st.session_state.messages.append({
        "role": "assistant",
        "content": f"🤖 开始每日任务: {task}"
    })

    # ==============================
    # 读取历史系统（关键）
    # ==============================

    memories = memory
    experiences = load_experience()
    reflections = load_reflection()

    # ==============================
    # 基于历史进行规划
    # ==============================

    enhanced_task = f"""
用户长期记忆：
{memories}

历史经验：
{experiences}

历史反思：
{reflections}

当前任务：
{task}

请基于以上信息优化执行策略。
"""

    plan = plan_task(enhanced_task)

    st.session_state.messages.append({
        "role": "assistant",
        "content": f"🧠 任务计划:\\n{plan}"
    })

    # ==============================
    # 执行步骤
    # ==============================

    steps = plan.split("\\n")

    results = []

    for step in steps:

        if "STEP" in step:

            st.session_state.messages.append({
                "role": "assistant",
                "content": f"⚙️ 执行: {step}"
            })

            result = execute_step(step)

            results.append(f"{step} → {result}")

            # ===== trace =====
            log_trace(step, result)

    # ==============================
    # 汇总结果
    # ==============================

    final_result = "\\n".join(results)

    # ==============================
    # 更新长期记忆（关键）
    # ==============================

    update_memory(task)

    # ==============================
    # 保存log
    # ==============================

    log_task(task, final_result)

    # ==============================
    # 总结经验（学习）
    # ==============================

    summarize_experience(task, final_result)

    # ==============================
    # 反思（自我优化）
    # ==============================

    reflection = reflect(task, final_result)

    # ==============================
    # AI自评（推荐）
    # ==============================

    score = evaluate_result(task, final_result)

    # ==============================
    # 保存日报
    # ==============================

    save_report(
        task,
        final_result,
        reflection + f"\\n\\n评分:\\n{score}"
    )

    # ==============================
    # UI展示
    # ==============================

    st.session_state.messages.append({
        "role": "assistant",
        "content": f"""
✅ 每日任务完成

📊 执行结果:
{final_result}

🧠 反思:
{reflection}

⭐ 评分:
{score}
"""
    })
# ======================================
# 定时任务注册
# ======================================

def schedule_daily_task(task, hour=9, minute=0):
    scheduler.add_job(
        autonomous_task,
        'cron',
        hour=hour,
        minute=minute,
        args=[task]
    )

# ===== Session =====
if "messages" not in st.session_state:
    st.session_state.messages = []



# ======================================
# 工具区
# ======================================
def summarize_experience(task, result):
    prompt = f"""
你是一个AI学习系统。

请从以下任务中总结经验教训：

任务：
{task}

执行结果：
{result}

请输出：
1. 成功的原因
2. 失败的原因（如果有）
3. 下次如何优化（最重要）

简洁输出：
"""

    summary = llm.invoke(prompt)

    with open(EXPERIENCE_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n=== 新经验 ===\n{summary}\n")

    return summary

def log_trace(step, result):
    data = {
        "step": step,
        "result": str(result)
    }

    try:
        with open(TRACE_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(data)

    with open(TRACE_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def evaluate(task, result):
    prompt = f"""
    请对任务执行质量评分（0-10）：

    任务：
    {task}

    结果：
    {result}

    输出：
    score:
    reason:
    """

    return llm.invoke(prompt)



def reflect(task, result):
    prompt = f"""
你是一个高级AI Agent。

请对以下任务执行进行反思：

任务：
{task}

执行结果：
{result}

请分析：
1. 任务是否成功（是/否 + 原因）
2. 哪一步最关键
3. 是否有错误或低效步骤
4. 如何优化策略（非常重要）

输出格式：
- success:
- key_step:
- issue:
- improvement:
"""

    reflection = llm.invoke(prompt)

    with open(REFLECTION_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n=== Reflection ===\n{reflection}\n")

    return reflection


def log_task(task, result):
    with open("task_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n任务: {task}\n结果: {result}\n")
        
def update_memory(user_input):
    global memory

    prompt = f"""
从用户输入中提取长期有用的信息（兴趣、目标、背景）。

只返回JSON，例如：
{{"interest": "AI", "goal": "写论文"}}

用户输入：
{user_input}
"""

    result = llm.invoke(prompt)

    try:
        new_data = eval(result)  # 简化版（够用）
        memory.update(new_data)
        save_memory(memory)
    except:
        pass

    
def load_reflection():
    try:
        with open(REFLECTION_FILE, "r", encoding="utf-8") as f:
            return f.read()[-2000:]
    except:
        return ""
    

def read_webpage(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.extract()

        text = soup.get_text(separator="\n")

        # 👉 分块
        chunk_size = 2000
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

        return chunks[:5]  # 最多5块（避免爆token）

    except Exception as e:
        return f"读取失败: {e}"

def search_and_read(query):
    urls = search_web(query)

    all_text = []

    for url in urls[:3]:
        chunks = read_webpage(url)
        all_text.extend(chunks)

    return all_text



def summarize_chunks(chunks):
    partial_summaries = []

    for i, chunk in enumerate(chunks):
        prompt = f"总结以下第{i+1}部分内容：\n{chunk}"
        summary = llm.invoke(prompt)
        partial_summaries.append(summary)

    # 👉 再汇总
    final_prompt = f"""
请综合以下总结，给出一个完整总结：

{chr(10).join(partial_summaries)}
"""
    final_summary = llm.invoke(final_prompt)

    return final_summary


    
def search_web(query):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=8):
            results.append(r["href"])
    return results

def open_notepad():
    os.system("notepad")
    return "已打开记事本"


def open_browser():
    subprocess.Popen("start chrome", shell=True)
    return "已打开浏览器"


def list_files():
    return "\n".join(os.listdir('.'))


def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("")
    return f"已创建文件 {filename}"


def write_code(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"代码已写入 {filename}"


def run_python(filename):
    return subprocess.getoutput(f"python {filename}")

def summarize(text):
    prompt = f"请用中文总结以下内容的重点：\n{text}"
    return llm.invoke(prompt)

def load_experience():
    try:
        with open(EXPERIENCE_FILE, "r", encoding="utf-8") as f:
            return f.read()[-2000:]  # 限制长度
    except:
        return ""
    
def load_logs():
    try:
        with open("task_log.txt", "r", encoding="utf-8") as f:
            return f.read()[-2000:]
    except:
        return ""
# ======================================
# Excel分析
# ======================================

def analyze_excel(file):
    df = pd.read_excel(file)
    summary = df.describe().to_string()
    return f"数据分析结果:\n{summary}"


# ======================================
# 任务规划
# ======================================
def plan_task(user_input):
    prompt = f"""
你是一个会自我优化的AI Agent。

用户长期信息：
{memory}

历史经验：
{load_experience()}

历史反思（非常重要）：
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
- create_file
- write_code
- run_python

输出：
STEP1: ...
STEP2: ...

任务：{user_input}
"""
    return llm.invoke(prompt)

# ======================================
# 执行器
# ======================================

def execute_step(step):
    try:
        step = step.lower()

        if "open_notepad" in step:
            return open_notepad()

        if "open_browser" in step:
            return open_browser()

        if "list_files" in step:
            return list_files()

        if "create_file" in step:
            parts = step.split()
            if len(parts) >= 2:
                return create_file(parts[-1])

        if "write_code" in step:
            return write_code("generated.py", "print('hello from AI')")

        if "run_python" in step:
            return run_python("generated.py")

        if "search_web" in step:
            query = step.replace("search_web", "").strip()
            urls = search_web(query)
            return urls
        
        if "read_web" in step:
            url = step.split()[-1]
            chunks = read_webpage(url)
            return summarize_chunks(chunks)

        
        if "summarize" in step:
            return summarize(step)
        
        if "search_and_read" in step:
            query = step.replace("search_and_read", "").strip()
            return search_and_read(query)
        
    except Exception as e:
        return f"失败: {e}"
    return "无法执行该步骤"

# ======================================
# UI：聊天气泡
# ======================================

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
# ======================================
# UI逻辑（替代while True）
# ======================================

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("请输入你的指令：")

# 文件上传
uploaded_file = st.file_uploader("上传Excel文件", type=["xlsx"])
if uploaded_file:
    result = analyze_excel(uploaded_file)
    st.session_state.messages.append({"role": "assistant", "content": result})

if st.button("执行"):
    if user_input:
        update_memory(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # ===== 简单指令（规则优先） =====
        if "记事本" in user_input:
            result = open_notepad()
            st.session_state.history.append((user_input, result))

        elif "浏览器" in user_input:
            result = open_browser()
            st.session_state.history.append((user_input, result))

        else:
            # ===== 复杂任务 =====
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

                    status_box.markdown(f"🧠 执行: {step} (尝试 {retry+1})")

                    result = execute_step(step)
                    log_trace(step, result)
                    
                    # 判断失败
                    if result is None or "失败" in str(result) or "无法执行" in str(result):
                        retry += 1

                        # 👉 自动修复（核心）
                        fix_prompt = f"""
        原步骤执行失败：
        {step}

        错误：
        {result}

        请修复这个步骤，只返回新的STEP格式
        """
                        step = llm.invoke(fix_prompt)

                    else:
                        success = True
                        results.append(f"✅ {step} → {result}")
                        status_box.markdown(f"✅ 完成: {step}")

                if not success:
                    results.append(f"❌ 最终失败: {step}")

            final_result = f"🧠 任务计划:\n{plan}\n\n⚙️ 执行结果:\n" + "\n".join(results)

            log_task(user_input, final_result)
            summarize_experience(user_input, final_result)
            reflect(user_input, final_result)
            score = evaluate(user_input, final_result)
            
            st.write("📊 评分:", score)

            st.session_state.history.append((user_input, final_result))
            
            st.rerun()
# ======================================
# 展示对话历史（类似聊天）
# ======================================

for q, a in reversed(st.session_state.history):
    st.markdown(f"**你:** {q}")
    st.markdown(f"**AI:** {a}")
    st.markdown("---")


schedule_daily_task(
    "帮我搜索最新AI新闻并总结",
    hour=9,
    minute=0
)


