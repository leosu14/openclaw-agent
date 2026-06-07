


def evaluate_result(task, result):
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