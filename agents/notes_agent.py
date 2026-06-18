from llm.llm_client import ask_llm


def generate_teacher_notes(
    level,
    lesson
):

    prompt = f"""
你是一位经验丰富的西班牙语教师培训专家。

下面是一份课程PPT：

{lesson}

请生成教师讲稿。

要求：

对于每一页：

提供：

1. 教学目标
2. 教师讲解建议
3. 提问建议
4. 预计学生回答
5. 课堂延伸建议

输出格式：

# Slide

标题：

教学目标：

教师讲解：

提问：

预计回答：

延伸：

等级：

{level}

使用中文说明教师行为。

学生内容保持西班牙语。
"""

    return ask_llm(prompt)