from agents.base_agent import BaseAgent
from config.prompt_builder import build_quiz_prompt


class QuizAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Quiz",
            prompt_builder=build_quiz_prompt,
            model_name="quiz"
        )

    def after_run(self, response, context):

        context.quiz = response

        context.history.append({
            "agent":"Quiz"
        })

        return response