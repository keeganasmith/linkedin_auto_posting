from dotenv import load_dotenv
import os
import requests
import time
import logging
import concurrent.futures
from openai import OpenAI
logging.basicConfig(level=logging.INFO)

load_dotenv()
class OpenAI_Client:
    def __init__(self, model = "gpt-3.5-turbo"):
        self.model = model
        self.client = OpenAI()
    def prompt_openai(self, prompt):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a skilled programmer who is in charge of providing a fun programming fact of the day for the companies linkedin account."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
        #return self.make_request("chat/completions", data).json()["choices"][0]["message"]["content"]
    
    def get_responses(self, prompts, special_additions = ""):
        responses = [""] * len(prompts)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for prompt in prompts:
                futures.append(executor.submit(self.prompt_openai, prompt + special_additions))

            concurrent.futures.wait(futures)
            i = 0
            for response in futures:
                responses[i] = response.result()
                i += 1
            
        return responses
# client = OpenAI_Client()
# text_response = client.prompt_openai("give me a fun fact about python")
# print(text_response)
