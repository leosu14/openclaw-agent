from llm.llm_client import ask_llm


def generate_lesson(level, topic, text):

    prompt = f"""
你是一位资深西班牙语教师和DELE考官。

你的任务：

根据新闻内容生成一份现代化西班牙语课堂PPT。

风格参考：

- Google NotebookLM
- Canva Education
- Aula Internacional
- DELE课堂

====================================

学生等级：

{level}

课堂主题：

{topic}

新闻内容：

{text}

====================================

请严格按照以下结构输出：

SLIDE:
TYPE: cover
TITLE:
IMAGE:
CONTENT:

SLIDE:
TYPE: warmup
TITLE:
IMAGE:
CONTENT:

SLIDE:
TYPE: image
TITLE:
IMAGE:
CONTENT:

SLIDE:
TYPE: vocab
TITLE:
IMAGE:
CONTENT:

SLIDE:
TYPE: reading
TITLE:
CONTENT:

SLIDE:
TYPE: grammar
TITLE:
CONTENT:

SLIDE:
TYPE: speaking
TITLE:
CONTENT:

SLIDE:
TYPE: summary
TITLE:
CONTENT:

SLIDE:
TYPE: homework
TITLE:
CONTENT:

====================================

要求：

【cover】

- 课程标题
- 主题图片关键词

【warmup】

2-3个导入问题

【image】

图片观察活动

例如：

- ¿Qué ves?
- ¿Quiénes aparecen?
- ¿Qué está pasando?

【vocab】

5-8个核心词汇

格式：

- ⚽ gol = goal
- 🏟 estadio = stadium

【reading】

根据新闻重新编写阅读材料

A1:
40-60词

A2:
80-120词

B1:
150-200词

使用符合等级的语言

【grammar】

提取一个最重要语法点

并设计一个简单练习

例如：

ganar → ganó

Completa:

Ayer Real Madrid _____.

【speaking】

设计3-5个口语问题

【summary】

输出：

🧠 Ideas Clave

3条最重要内容

【homework】

设计一个课后任务

====================================

等级要求：

A1：

- 简单句
- 高频词汇
- 图片优先
- 少语法

A2：

- 增加阅读
- 增加表达

B1：

- 增加讨论
- 增加观点表达
- 接近DELE B1

====================================

输出规则：

1. 必须使用西班牙语

2. 不要解释

3. 不要输出Markdown

4. 严格保持：

SLIDE:
TYPE:
TITLE:
IMAGE:
CONTENT:

格式

5. 每页最多5个项目

6. 图片关键词必须是英文
"""

    return ask_llm(prompt)