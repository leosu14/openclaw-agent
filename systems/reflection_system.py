from llm.llm_client import ask_llm

REFLECTION_FILE = "data/reflection.txt"

def load_reflection():

    try:

        with open(
            REFLECTION_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()[-2000:]

    except:

        return ""

def reflect(task, result):

    prompt = f"""
你是一个高级AI Agent。

请对以下任务执行进行反思：

任务：
{task}

执行结果：
{result}

请分析：

1. 任务是否成功
2. 哪一步最关键
3. 是否有错误或低效步骤
4. 如何优化策略

输出格式：

- success:
- key_step:
- issue:
- improvement:
"""

    reflection = ask_llm(prompt)

    with open(
        REFLECTION_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"\\n=== Reflection ===\\n{reflection}\\n"
        )

    return reflection