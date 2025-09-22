import streamlit as st
import openai

API_KEY="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"

client=openai.OpenAI(api_key=API_KEY)
#storing the chat hhistory

if"message" not in st.session_state:
    st.session_state["messages"]=[]
    
st.title("It's My Bot")

#show the chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])
    
#user input
prompt = st.chat_input("let's begin.... ")
if prompt:
    st.session_state['messages'].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)
    response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=st.session_state['messages'],
          max_tokens=300,
          temperature=0.7
    )
    
    reply=response.choices[0].message.content
    st.session_state["messages"].append({"role":"assistant","content":reply})
    st.chat_message("assistant").markdown(reply)
    
    
   

