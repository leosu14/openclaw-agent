from abc import ABC, abstractmethod

from llm.llm_client import ask_llm


class BaseAgent(ABC):

    def __init__(

        self,

        name,

        prompt_builder,

        model_name

    ):

        self.name = name

        self.prompt_builder = prompt_builder

        self.model_name = model_name

    def run(self, context):

        prompt = self.prompt_builder(
            context
        )

        response = ask_llm(

            prompt,

            model=self.model_name

        )

        return self.after_run(

            response,

            context

        )

    @abstractmethod
    def after_run(

        self,

        response,

        context

    ):

        pass