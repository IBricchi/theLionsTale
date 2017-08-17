from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            current_user = request.user
            newAuthor = current_user.author_set.create(name = current_user.first_name + " " + current_user.last_name)
            newAuthor.save()
            return redirect('authorIndex')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
