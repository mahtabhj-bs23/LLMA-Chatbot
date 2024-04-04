import os

from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
#from langchain.chains import ConverstationChain

def demo_chatbot():
    demo_llm = Bedrock(
        model_id='meta.llama2-13b-chat-v1:0:4k',
        model_kwargs= {
        "temperature": 0.9,
        "top_p": 0.5,
        "max_gen_len": 512})
