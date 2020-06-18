from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.models import Member


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password1']
            phone_number = request.POST['phone-number']

            user = User.objects.create_user(email=email, username=username, password=password)
            user.member.phone_number = phone_number
            user.save()

            auth.login(request, user)
            return redirect("/")
    return render(request, "accounts/signup.html")


def list_member(request):
    members = Member.objects.all()
    return render(request, "accounts/members_list.html", {"members": members})