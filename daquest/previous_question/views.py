from django.shortcuts import render

from questions.models import Questions, Comments


def previous_question(request):
    questions = Questions.objects.all().order_by('-published_date')
    context = {"questions": questions}
    return render(request, 'question/previous.html', context)
