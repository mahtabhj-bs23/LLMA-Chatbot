# from langchain.chains import LLMChain
# from langchain.llms.bedrock import Bedrock
# from langchain.prompts import PromptTemplate
# import boto3
# import os
# import streamlit as st

# os.environ["AWS_PROFILE"] = "Mahtab"

# #bedrock client

# bedrock_client = boto3.client(
#     service_name="bedrock-runtime",
#     region_name="us-east-1"
# )

# modelID = "meta.llama2-13b-chat-v1"


# llm = Bedrock(
#     model_id=modelID,
#     client=bedrock_client,
#     model_kwargs={"temperature":0.9}
# )

# def my_chatbot(language,freeform_text):
#     prompt = PromptTemplate(
#         input_variables=["language", "freeform_text"],
#         template="You are a chatbot. You are in {language}.\n\n{freeform_text}"
#     )

#     bedrock_chain = LLMChain(llm=llm, prompt=prompt)

#     response=bedrock_chain({'language':language, 'freeform_text':freeform_text})
#     return response

# #print(my_chatbot("english","who is buddha?"))

# st.title("Cloud-23 Chatbot")

# language = st.sidebar.selectbox("Language", ["english", "bengali"])

# if language:
#     freeform_text = st.sidebar.text_area(label="what is your question?",
#     max_chars=100)

# if freeform_text:
#     response = my_chatbot(language,freeform_text)
#     st.write(response['text'])

from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate
import boto3
import os
import streamlit as st

os.environ["AWS_PROFILE"] = "Mahtab"

# Bedrock client
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

modelID = "meta.llama2-13b-chat-v1"

llm = Bedrock(
    model_id=modelID,
    client=bedrock_client,
    model_kwargs={"temperature": 0.7}  # Adjust temperature as needed
)

def my_chatbot(question):
    prompt = PromptTemplate(
        input_variables=["question"],
        template="{question}"
    )

    bedrock_chain = LLMChain(llm=llm, prompt=prompt)

    response = bedrock_chain({'question': question})
    return response['text']

st.title("Cloud-23 Chatbot")

# Text area for user input
question = st.text_area(label="What is your question?", max_chars=100)

# Enter button
if st.button("Enter"):
    if question:
        response = my_chatbot(question)
        # Display the response in a scrollable text area
        st.text_area(label="Response", value=response, height=300, max_chars=5000, key='response')

# Reposition the sidebar to the bottom of the screen
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            bottom: 50px;
            position: fixed;
            width: 20rem; /* Adjust the width as needed */
        }
    </style>
    """,
    unsafe_allow_html=True
)
