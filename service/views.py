# -*- coding: utf-8 -*-
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from service.forms import AnswerForm
from service.models import Test, ActiveTest, Answer


def registration(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'service/registration.html', {'form': form})


@login_required
def home(request):
    qset = Test.objects.all()
    return render(request, 'service/home.html', {'qset': qset})


@login_required
def do_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    active_test = ActiveTest.objects.get_or_create(user=request.user, test=test)[0]
    already_done = active_test.results.keys()
    question = test.questions.exclude(id__in=already_done).first()
    for p in Answer.objects.raw('SELECT * FROM service_answer'):
        print(p)
    if not question:
        good_answers = 0

        for k in active_test.results.values():
            for v in k:
                if v.get('is_true'):
                    good_answers += 1

        return render(request, 'service/results.html', {
            'active_test': active_test,
            'good_answers': good_answers,
        })

    form = AnswerForm(request.POST or None, answers=question.answers.all())
    if form.is_valid():
        active_test.results[question.id] = list(form.cleaned_data['answers'].values('is_true'))
        active_test.save()
        return redirect('do_test', test_id)

    return render(request, 'service/do_test.html', {
        'test': test,
        'active_test': active_test,
        'question': question,
        'form': form,
    })


# @login_required
# def chat(request):
#     form = MessageForm(request.POST or None)
#     if request.method == "POST" and request.is_ajax:
#         if form.is_valid:
#             message = Message.objects.get_or_create(user=request.user, text=request.POST['text'])[0]
#             message.save()
#             return redirect('chat')
#     return render(request, 'service/chat.html', {'form': form, 'message': message})
