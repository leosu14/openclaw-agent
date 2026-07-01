from agents.base_agent import BaseAgent
from config.prompt_builder import build_notes_prompt


class NotesAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Notes",
            prompt_builder=build_notes_prompt,
            model_name="notes"
        )

    def after_run(self, response, context):

        context.notes = response

        context.history.append({
            "agent":"Notes"
        })

        return response