import logging
from django.db import DatabaseError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from . import ai
from .forms import QuestionForm
from .models import Message

HISTORY_SIZE = 10

logger = logging.getLogger(__name__)


@require_GET
def index(request):
    answer = None
    answer_id = request.GET.get('answer', '')
    if answer_id.isdigit():
        answer = Message.objects.filter(pk=answer_id).first()

    return _render(request, QuestionForm(), answer=answer)


@require_POST
def chat(request):
    form = QuestionForm(request.POST)
    question = form.cleaned_data['question']
    answer_text = ai.ask(question)
    message = Message.objects.create(user_text=question, ai_text=answer_text)
    
    return redirect(f"{reverse('chat:index')}?answer={message.pk}")


def _render(request, form, *, answer=None, error=None, status=200):
    history = list(Message.objects.all()[:HISTORY_SIZE])
    context = {'form': form, 'answer': answer, 'error': error, 'history': history}
    
    return render(request, 'chat/index.html', context, status=status)