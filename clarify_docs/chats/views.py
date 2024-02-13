from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import Chat, File, Question, Answer, Request
from llm_chat.models import UserData
from .data_extractor import read_file
from .qa_model import QAModel
from .elasticsearch_crud import record_context, connection


@login_required
def main(request):
    user = UserData.objects.filter(id = request.user.id).get()
    user_chats = [chat for chat in Chat.objects.filter(user_id=user).all()]

    if request.method == 'POST' and request.FILES.getlist('myfile'):
        files = request.FILES.getlist('myfile')
        chat = Chat(user=user)
        user_chats.append(chat)
        chat.save()
        text = ''
        for file in files:
            if file is not None:
                if file.content_type in ['application/pdf', 'application/msword',
                                         'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                         'text/plain']:
                    text += read_file(file)
                    new_file = File(filename=file.name, chat=chat)
                    new_file.save()
        record_context(chat.id, text, connection)

    return render(request, 'chats/index.html', {'chats': user_chats})


@login_required
def chat_detail(request, chat_id):
    user = UserData.objects.filter(id = request.user.id).get()
    current_chat = Chat.objects.filter(id=chat_id).get()
    user_chats = [chat for chat in Chat.objects.filter(user_id=user).all()]

    if current_chat.user != user:
        return redirect("/chats", {'chats': user_chats})
    
    requests = [request_ for request_ in Request.objects.filter(chat=current_chat)]
    if request.method == "POST":
        question = Question(chat=current_chat, text=request.POST["text"])
        question.save()
        
        model = QAModel(chat_id)
        # print("hhhhhhhhhhhhhhhhhhhhh", question.text)
        answer_text = model.get_answer(question.text)

        answer = Answer(chat=current_chat, text=answer_text)
        answer.save()

        request_ = Request(chat=current_chat, question=question, answer=answer)
        requests.append(request_)
        request_.save()
        
    return render(request, 'chats/chat_interaction.html', {'chat_id': chat_id, 'chats': user_chats, 'requests': requests})
