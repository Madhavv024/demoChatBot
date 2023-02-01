from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=0.9)
keep_prompting = True
while keep_prompting:
    prompt = input('What is your questions? Type exit if done-- \n')
    if prompt=='exit':
        keep_prompting = False
    else:
        print(llm(prompt))