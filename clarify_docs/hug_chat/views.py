from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from llm_chat.models import UserData
from .models import HugChatMessage
from .hug_model import get_answer, get_list, create_conversation


@login_required
def hug_chat(request):
    user_data = request.user
    try:
        user = UserData.objects.get(user=user_data)
    except UserData.DoesNotExist:
        user = UserData.objects.create(user=user_data, total_files_uploaded=0, total_questions_asked=0)

    # user = UserData.objects.filter(id=request.user.id).get()
    requests = [request_ for request_ in HugChatMessage.objects.filter(user_id=user.id).all()]

    message_list = get_list()

    if request.method == "POST":
        if 'create-new-chat' in request.POST:
            create_conversation()
            message = 'Hello!'
            answer = get_answer(message)
        else:
            message = request.POST["text"]
            answer = get_answer(message)
        request_ = HugChatMessage(user_id=user.id, message=message, answer=answer)
        requests.append(request_)
        request_.save()

    return render(request, 'hug_chat/chat_hug.html', {'requests': requests, "msg_list": message_list})


