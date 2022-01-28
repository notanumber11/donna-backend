from src.open_ai_facade import OpenAIFacade

def default_call():
    open_ai_facade = OpenAIFacade()
    customer_prompt = "I would like to have a meeting tomorrow. \n\n" \
                      "I can talk about our books and movies. We have several discounts. " \
                      "I am available from 9 to 10 pm. Thanks"
    rewrite_type = "creative"
    response = open_ai_facade.get_answer_customer_prompt(customer_prompt, rewrite_type)
    print("The response is: " + response)
    return response

if __name__ == "__main__":
    default_call()