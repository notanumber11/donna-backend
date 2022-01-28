from src.open_ai_api import OpenAIapi
from src.timer import timeit


class OpenAIFacade:

    def __init__(self):
        print("Starting OpenAIFacade")
        self.open_ai_api = OpenAIapi()

    @timeit
    def get_answer_customer_prompt(self, customer_prompt:str, rewrite_type:str) -> str:
        try:
            full_answer = self.open_ai_api.call_open_ai_with_customer_prompt(customer_prompt, rewrite_type)
            str_answer = full_answer.choices[0].text
            str_answer= str_answer.strip()
            print("The open_ai first answer is={}".format(str_answer))
            return str_answer
        except Exception as e:
            print("Problems calling openAI: " + str(e))
            return "Problems calling openAI"

    @timeit
    def get_answer_full_prompt(self, full_prompt:str) -> str:
        full_answer = self.open_ai_api.call_open_ai_with_full_prompt(full_prompt)
        str_answer = full_answer.choices[0].text
        return str_answer
