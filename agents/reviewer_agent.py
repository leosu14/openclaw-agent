from agents.base_agent import BaseAgent
from config.prompt_builder import build_reviewer_prompt


class ReviewerAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Reviewer",
            prompt_builder=build_reviewer_prompt,
            model_name="reviewer"
        )

    def after_run(self, response, context):

        context.review = response

        context.history.append({
            "agent":"Reviewer"
        })

        return response