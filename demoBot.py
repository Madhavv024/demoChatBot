from langchain.llms import OpenAI
import os
import streamlit as st
from streamlit_chat import message
os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI(temperature=0.9)

def get_ans(user_input):
    ans = llm(user_input)
    print(ans)
    return ans

st.title("ChatBot")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = get_ans(user_input)
    #store the input and output
    st.session_state.past.append(user_input) 
    st.session_state.generated.append(output)

if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')