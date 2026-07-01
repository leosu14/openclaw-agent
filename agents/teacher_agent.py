from agents.base_agent import BaseAgent
from config.prompt_builder import build_teacher_prompt


class TeacherAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Teacher",
            prompt_builder=build_teacher_prompt,
            model_name="teacher"
        )

    def after_run(self, response, context):
        context.lesson = response

        context.history.append({
            "agent": "Teacher",
            "slides": response.count("SLIDE")
        })

        return response 