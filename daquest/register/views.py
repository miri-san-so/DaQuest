from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
from .forms import RegisterForm


@cache_page(60 * 15)
@csrf_protect
def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/question")
    else:
        form = RegisterForm()
    return render(response, 'question/signup.html', {"form": form})
