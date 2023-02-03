from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
import os
import streamlit as st
from streamlit_chat import message
from langchain import PromptTemplate

def open_file(filepath):
    with open(filepath,'r',encoding='utf-8') as infile:
        return infile.read()

template = open_file('promp_chat.txt')

prompt = PromptTemplate(
    input_variables=["Chandler"],
    template=template,
)

os.environ["OPENAI_API_KEY"] = open_file('api_key.txt')
llm = OpenAI(temperature=0.6)

conversation_with_summary = ConversationChain(
    llm=llm, 
    # We set a low k=3, to only keep the last 3 interactions in memory
    memory=ConversationBufferWindowMemory(k=3), 
    verbose=False
)


def get_ans(user_input):
    ans = conversation_with_summary.predict(input=user_input)
    # print(ans) #to check ans 
    return ans.strip()

st.title("Chandler the Bot")

# if 'generated' not in st.session_state:
#     st.session_state['generated'] = []

# if 'past' not in st.session_state:
#     st.session_state['past'] = []



def get_text():
    input_text = input("Enter your ques here: ")
    # input_text = st.text_input("You: ", key="input")
    return input_text


user_input = ""

while(user_input!="bye"):
    user_input = get_text()
    # if user_input:
    output = get_ans(user_input)
    print("Chandler: "+output)
    # st.session_state.past.append(user_input) 
    # st.session_state.generated.append(output)
    
    
# if st.session_state['generated']:
#     for i in range(len(st.session_state['generated'])-1, -1, -1):
#         message(st.session_state["generated"][i], key=str(i))
#         message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

