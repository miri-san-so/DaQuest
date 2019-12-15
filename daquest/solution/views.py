from django.shortcuts import render
from questions.models import Solutions, Questions
#from daquest.questions.models import Solutions, Questions

# Create your views here.


def solution(request):
    latest_question = Questions.objects.latest('published_date')
    solution_text = Solutions.objects.filter(question=latest_question.id)
    context = {'latest_question': latest_question, 'solutions': solution_text}

    return render(request, 'question/solution.html', context)
