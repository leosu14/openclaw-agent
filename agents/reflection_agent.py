from agents.base_agent import BaseAgent
from config.prompt_builder import build_reflection_prompt


class ReflectionAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Reflection",
            prompt_builder=build_reflection_prompt,
            model_name="reflection"
        )

    def after_run(self, response, context):

        context.reflection = response

        context.history.append({
            "agent":"Reflection"
        })

        return response