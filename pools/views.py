from django.shortcuts import render, redirect
from pools.models import Question
from pools.models import Choice
from django.http import request

# Create your views here.


def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, "index.html", {'questions': questions})

def question(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, "question.html", {'question': question})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, "choices.html", {'question': question})

def choose(request, question_id, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.vote()
    return redirect(question, question_id=question_id)

def results(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, "results.html", {'question': question})

def manage(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, "manage.html", {'question': question})
