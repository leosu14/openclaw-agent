from llm.llm_client import ask_llm


def generate_lesson(level, topic, article_text):
    prompt = f"""
你是一位世界级西班牙语教师。

请生成：

Google NotebookLM + Canva 风格 的 PPT 教案。

要求：

1. 每页 PPT 内容不能太多
2. 每页最多 5 行
3. 内容适合视觉展示
4. 风格现代化
5. 有 emoji
6. 有课堂互动
7. 有图片讨论页
8. 有词汇页
9. 有阅读页
10. 有总结页

必须严格按下面格式输出：

SLIDE:
TYPE: vocab
TITLE: 📚 Vocabulario
IMAGE: football players
CONTENT:
- jugador
- equipo
- estadio

SLIDE:
TYPE: discussion
TITLE: 🗣️ Hablemos
IMAGE: football fans
CONTENT:
- ¿Te gusta el fútbol?
- ¿Qué equipo prefieres?


等级：
{level}

主题：
{topic}

新闻：
{article_text}
"""
    return ask_llm(prompt)