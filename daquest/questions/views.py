from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from .models import Questions, Comments

from .forms import CommentForm

# Get Question and Display


def index(request):

    # Give Latest Question
    latest_question = Questions.objects.latest('published_date')
    context = {"latest_question": latest_question}

    # Get Comments for current question
    comments = Comments.objects.filter(question=latest_question.id)
    context['comments'] = comments
    context['form'] = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                question=latest_question,
                author=form.cleaned_data["author"],
                comment_text=form.cleaned_data["body"],
            )
            comment.save()
        return HttpResponseRedirect('/')

    return render(request, 'question/index.html', context)
