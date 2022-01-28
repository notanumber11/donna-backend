from src.open_ai_api import OpenAIapi
from src.open_ai_facade import OpenAIFacade

print("Starting app.py")
open_ai_facade = OpenAIFacade()


def handler(event, context):
    print("Handler received the event")
    return execute(event)

def validate(event):
    if not "customer_prompt" in event:
        raise ValueError("Expected customer_prompt in the request")
    customer_prompt = event["customer_prompt"]
    if len(customer_prompt) > 10000:
        raise ValueError("Too big prompt")
    if not "rewrite_type" in event:
        raise ValueError("Expected rewrite_type in the request")
    rewrite_type = event["rewrite_type"]
    if rewrite_type not in OpenAIapi.valid_prompts:
        raise ValueError("Expected rewrite_type is incorrect")
    return customer_prompt, rewrite_type

def execute(event):
    try:
        print("Starting request with event={}".format(event))
        customer_prompt, rewrite_type = validate(event)
        response = open_ai_facade.get_answer_customer_prompt(customer_prompt, rewrite_type)
        print("Finished request with response={}".format(response))
    except Exception as e:
        print("Problems calling lambda: " + str(e))
        return "Problems calling lambda"
    return response
