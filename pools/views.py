from django.shortcuts import render, redirect
import datetime
from pools.models import Question
from pools.models import Category
from pools.models import Choice
from pools.forms import NewQuestionForm

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
    return render(request, "results.html", {'question': question, 'question_id': question_id})


def manage(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, "manage.html", {'question': question})


def new_question(request):
    if request.method == "POST":
        question_form = NewQuestionForm(data=request.POST)
        redirect_to = request.POST.get("redirect_to", "/")
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.pub_date = datetime.datetime.now()
            question.save()
            question_form.save_m2m()
            return redirect('question', question_id=question.id)
        return render(request, 'new_question.html', {'question_form': question_form})
    else:
        question_form = NewQuestionForm()
        return render(request, "new_question.html", {'question_form': question_form})


def edit_question(request, question_id):
    if request.method == "POST":
        question_form = NewQuestionForm(data=request.POST, instance=Question.objects.get(id=question_id))
        redirect_to = request.POST.get("redirect_to", "/")
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.save()
            question_form.save_m2m()
            return redirect('question', question_id=question.id)
        return render(request, 'new_question.html', {'question_form': question_form})
    else:
        question_form = NewQuestionForm(instance=Question.objects.get(id=question_id))
        return render(request, "new_question.html", {'question_form': question_form})


def destroy_question(request, question_id):
    question = Question.objects.get(id=question_id)
    deleted = question.delete()
    if deleted:
        return redirect('index')
    else:
        return redirect('question', question_id=question.id)
