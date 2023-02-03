from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory , ConversationBufferMemory
import os
import streamlit as st
from streamlit_chat import message
from langchain import PromptTemplate , LLMChain
import gradio as gr

def open_file(filepath):
    with open(filepath,'r',encoding='utf-8') as infile:
        return infile.read()

template = template = """You are a Chandler having a conversation with a human.
Chandler is a AI bot that has a very good sense of humor, and is notoriously sarcasm.

{chat_history}
Human: {human_input}
Chandler:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template
)

os.environ["OPENAI_API_KEY"] = open_file('api_key.txt')
llm = OpenAI(temperature=0.6)

conversation_with_summary = LLMChain(
    llm=llm, 
    # We set a low k=3, to only keep the last 3 interactions in memory
    prompt=prompt,
    memory = ConversationBufferWindowMemory(memory_key="chat_history" , k=3), 
    verbose=True,
)


def get_ans(user_input):
    ans = conversation_with_summary.predict(human_input=user_input)
    # print(ans) #to check ans 
    return ans.strip()

#console-------------------------------

def get_text():
    human_input = input("Enter your ques here: ")
    # input_text = st.text_input("You: ", key="input")
    return human_input

user_input = ""

negatives = ["bye" , "cya" , "take care" , "bye bye" , "now bye"]

# while(user_input not in negatives):
#     user_input = get_text()
#     # if user_input:
#     output = get_ans(user_input)
#     print("Chandler: "+output)
    # st.session_state.past.append(user_input) 
    # st.session_state.generated.append(output)

#streamlit-------------------

# st.title("Chandler the Bot")

# if 'generated' not in st.session_state:
#     st.session_state['generated'] = []

# if 'past' not in st.session_state:
#     st.session_state['past'] = []
    
# if st.session_state['generated']:
#     for i in range(len(st.session_state['generated'])-1, -1, -1):
#         message(st.session_state["generated"][i], key=str(i))
#         message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
    
#gradio-------------------------------------------    
    
def chatbot(input , history=[] ):
    output = get_ans(input)
    history.append((input,output))
    return history , history

gr.Interface(fn = chatbot ,
             inputs = ["text" , 'state'],
             outputs = ["chatbot" , 'state']
             ).launch(debug = True) # share=True)
