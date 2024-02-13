import os
from hugchat import hugchat
from hugchat.login import Login

# from data_project_chat.settings import env
from dotenv import load_dotenv

load_dotenv()

sign = Login(os.getenv('HUGGING_EMAIL'), os.getenv('HUGGING_PASSWORD'))
cookies = sign.login()
sign.saveCookiesToDir()

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
chatbot.share_conversation()

def create_conversation() -> str:
    id_ = chatbot.new_conversation()
    chatbot.change_conversation(id_)
    return id_
#
#
# def get_answer(conversation_id: str, question: str) -> str:
#     chatbot.change_conversation(conversation_id)
#     answer = chatbot.chat(question)
#     return answer

def get_answer(question: str) -> str:
    answer = chatbot.chat(question)
    return answer

def get_list():
    info = chatbot.get_conversation_info()
    # print(info.id, info.title, info.model, info.system_prompt, info.history)
    return [info.id, info.title, info.model]