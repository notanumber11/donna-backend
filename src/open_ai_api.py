"""
    Responsible to interact with open ai service
"""
import os

import openai


class OpenAIapi:

    valid_prompts = {
        "creative" : {
            "prompt": "Rewrite this professionally:\n",
            "temperature": 0.7
        },
        "enhanced" : {
            "prompt": "Rewrite this professioally:\n",
            "temperature": 0.0
        }
    }

    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def __read_env_key__(self):
        pass

    def call_open_ai_with_customer_prompt(self, customer_prompt:str, rewrite_type:str):
        donna_prompt = OpenAIapi.valid_prompts[rewrite_type]["prompt"]
        temperature = OpenAIapi.valid_prompts[rewrite_type]["temperature"]
        full_prompt = '{}"{}"'.format(donna_prompt, customer_prompt)
        response = self.call_open_ai_with_full_prompt(full_prompt, temperature)
        return response

    def call_open_ai_with_full_prompt(self, full_prompt:str, temperature:float):
        print("Calling open_ai with temperature: {} and full prompt={}"
              .format(temperature, full_prompt))
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=full_prompt,
            temperature=temperature,
            max_tokens=512,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
        )
        print("Call to open_ai has finished")
        return response