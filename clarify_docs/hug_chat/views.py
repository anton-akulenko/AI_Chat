from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from llm_chat.models import UserData
from .models import HugChatMessage
from .hug_model import create_conversation, get_answer


@login_required
def hug_chat(request):
    user = UserData.objects.filter(id=request.user.id).get()
    requests = [request_ for request_ in HugChatMessage.objects.filter(user_id=user.id).all()]

    if request.method == "POST":
        message = request.POST["text"]
        answer = get_answer(create_conversation(), message)
        request_ = HugChatMessage(user_id=user.id, message=message, answer=answer)
        requests.append(request_)
        request_.save()

    return render(request, 'hug_chat/chat_hug.html', {'requests': requests})