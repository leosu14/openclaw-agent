from agents.base_agent import BaseAgent
from config.prompt_builder import build_planner_prompt


class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Planner",
            prompt_builder=build_planner_prompt,
            model_name="planner"
        )

    def after_run(self, response, context):
        context.plan = response
        context.history.append({
            "agent": "Planner",
            "status": "success"
        })
        return response