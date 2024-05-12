from openai_client.chatgpt import OpenAI_Client
from linkedin_api.linkedin_api import Linkedin
import pickle
import random
def remove_non_bmp(a: str):
    i =0
    print(a)
    while(i < len(a)):
        if(ord(a[i]) > 0xFFFF):
            a.replace(a[i], "")
        else:
            i += 1
    return a
def generate_post():
    prompts = []
    with open("./openai_client/prompts/prompts.pkl", "rb") as file:
        prompts = pickle.load(file)

    index = random.randint(0, len(prompts) - 1)
    prompt = prompts[index]
    ai_client = OpenAI_Client()
    message = ai_client.prompt_openai(prompt)
    message = remove_non_bmp(message)
    print("got here")
    li_client = Linkedin()
    li_client.make_post(message)
    del prompts[index]
    with open("./openai_client/prompts/prompts.pkl", "wb") as file:
        pickle.dump(prompts, file)

generate_post()

    
    

