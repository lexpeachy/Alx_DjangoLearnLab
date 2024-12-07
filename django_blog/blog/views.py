from django.shortcuts import render
from django.contrib.auth.views import loginview, logoutview
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decoraters import login_required



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            User=form.save()
            login(request,user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm
        return render(request, 'blog/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        User= request.user
        user.email = request.post.get('email', user.email)
        user.save()
        return redirect('profile')
    return render(request, 'profile.html')
