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


def create_conversation() -> str:
    id_ = chatbot.new_conversation()
    return id_


def get_answer(conversation_id: str, question: str) -> str:
    chatbot.change_conversation(conversation_id)
    answer = chatbot.chat(question)
    return answer