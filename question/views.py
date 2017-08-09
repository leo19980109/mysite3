from django.shortcuts import render_to_response
from question.models import Question

def index(request):
        questions = Question.objects.all()
        return render_to_response('index.html',{'questions': questions})

def question_detail(request, question_id):
        question = Question.objects.get(pk=question_id)
        return render_to_response('question_detail.html',{'question': question})