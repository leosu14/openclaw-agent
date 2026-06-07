from datetime import datetime
from tools.news_tools import search_news
from tools.news_tools import read_article
# from tools.image_tools import download_images
from tools.ppt_generator import create_ppt
from agents.teacher_agent import generate_lesson
from systems.memory_system import load_memory
from systems.reflection_system import reflect
from systems.evaluation_system import evaluate_result
from systems.trace_system import log_trace


LEVELS = ["A1", "A2", "B1"]

TOPICS = {
"A1": "weather football travel",
"A2": "technology tourism culture",
"B1": "AI society economy cinema"
}


def run_daily_teacher_agent():
    today = datetime.now().strftime("%Y-%m-%d")
    memory = load_memory()
    for level in LEVELS:
        topic = TOPICS[level]
        print(f"===== {level} =====")
        news = search_news(topic)

        if not news:
            continue
        article = read_article(news[0]["url"])
        lesson = generate_lesson(
        level,
        topic,
        article
        )
        # images = download_images(topic)
        output_path = (
        f"output/ppt/{level}_lesson_{today}.pptx"
        )
        create_ppt(
            f"{level} Lesson",
            lesson,
            output_path,
            # images 
        )
        log_trace(level, output_path)
        reflection = reflect(level, lesson)
        score = evaluate_result(level, lesson)
        print(reflection)
        print(score)
run_daily_teacher_agent()