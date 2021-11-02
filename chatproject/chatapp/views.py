from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .forms import CustomUserCreationForm
from .models import ChatMessages, Profile

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def room(request, room_name):
    chat_messages = ChatMessages.objects.filter(room_name=room_name)
    return render(request, 'room.html', {'room_name': room_name, 'chat_messages': chat_messages})

def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            fs = form.save(commit=False)
            emailvalue = form.cleaned_data.get("email")
            uservalue = form.cleaned_data.get("username")
            passwordvalue1 = form.cleaned_data.get("password1")
            passwordvalue2 = form.cleaned_data.get("password2")

            try:
                user = User.objects.get(username=uservalue)
                context = {'form': form,
                           'error': 'The username you entered has already been taken. Please try another username.'}
                return render(request, "users/register.html", context)

            except User.DoesNotExist:
                user = User.objects.create_user(uservalue, password=passwordvalue1, email=emailvalue)
            user_profile = Profile(user=user)
            user.save()
            user_profile.save()
            login(request, user)
            return redirect('index')
        return redirect('register')
@login_required
def profile(request, user_name):
    chat_messages = ChatMessages.objects.filter(room_name=user_name)
    user = User.objects.get(username=user_name)
    return render(request, 'profile.html', {'user_name': user, 'chat_messages':chat_messages})

@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):
    user.profile.is_online = True
    user.profile.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):
    user.profile.is_online = False
    user.profile.save()
