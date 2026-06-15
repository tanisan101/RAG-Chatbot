import streamlit as st
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq

load_dotenv()

st.title("⚖️ Legal Assistance Chatbot")

# Initialize clients
pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))
index_name = 'rag-chatbot'

llm = ChatGroq(
    groq_api_key=os.environ.get("GROQ_API_KEY"),
    model_name="llama3-8b-8192",  # ← FIXED (this is the chat model)
    temperature=0.1,
)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    else:
        with st.chat_message("assistant"):
            st.write(msg.content)

# Handle user input
if user_query := st.chat_input("Ask a legal question..."):

    with st.chat_message("user"):
        st.write(user_query)

    # Pinecone search
    query_embedding = pc.inference.embed(
        "llama-text-embed-v2",  # ← this is correct, embedding model
        inputs=[user_query],
        parameters={"input_type": "query"}
    )

    index = pc.Index(index_name)
    results = index.query(
        namespace="BNS",
        vector=query_embedding[0].values,
        top_k=2,
        include_values=False,
        include_metadata=True
    )

    context = " ".join([
        results["matches"][0]["metadata"]["text"],
        results["matches"][1]["metadata"]["text"],
    ])

    system_prompt = f"""
    You are an expert in the Indian Legal System. You are here to help the user with their queries.
    Based on the USER QUERY: {user_query} and the given CONTEXT: {context}, please provide a response.
    Guidelines:
    - Keep the answer short and to the point.
    - If you don't know the answer, say I don't know.
    - If you need more information, ask the user.
    """

    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content=system_prompt),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}")
    ])

    chain = prompt | llm

    response = chain.invoke({
        "history": st.session_state.messages,
        "input": user_query
    })

    st.session_state.messages.append(HumanMessage(content=user_query))
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)
