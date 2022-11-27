from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as loginuser , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home')

def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username , password = password)
            if user is not None:
                loginuser(request, user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request, 'login', context=context)

def signup(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        context = {
            'form' : form
        }
        return render(request, 'signup.html', context=context)

    else:
        print(request.POST)
        form = UserRegistrationForm(request.POST)
        context = {
            'form' : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect("login")

        else:
            return render(request, 'login', context=context)


def signout(request):
    logout(request)
    return redirect('home')