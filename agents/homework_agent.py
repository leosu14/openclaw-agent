from agents.base_agent import BaseAgent
from config.prompt_builder import build_homework_prompt


class HomeworkAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Homework",
            prompt_builder=build_homework_prompt,
            model_name="homework"
        )

    def after_run(self, response, context):

        context.homework = response

        context.history.append({
            "agent":"Homework"
        })

        return response