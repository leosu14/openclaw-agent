from llm.llm_client import ask_llm


def generate_lesson(level, topic, article_text):
    prompt = f"""
你是一位专业西班牙语教师。
请生成：
1. NotebookLM 风格教学内容
2. 适合 {level}
3. 分点清晰
4. PPT 风格排版
5. 适合视觉化呈现
6. 每页内容不要过多
7. 使用现代教学风格
必须包含：
# 标题
# 今日新闻
# 核心词汇
# 语法点
# 阅读练习
# 讨论问题
# 课堂互动
# 总结
新闻：
{article_text}
"""
    return ask_llm(prompt)