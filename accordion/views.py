from operator import ge
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from json import dumps

from .models import User, Post, Keyboard

keys = {"F": "q", "FS": "w", "G": "e", "GS": "r", "A": "t", "AS": "y", "B": "u", 
"C2": "i", "CS2": "o", "D2": "p", "DS2": "a", "E2": "s", "F2": "d", "FS2": "f", "G2": "g", "GS2": "h", "A2": "j", "AS2": "k", "B2": "l",
"C3": "z", "CS3": "x", "D3": "c", "DS3": "v", "E3": "b", "F3": "n", "FS3": "m", "G3": "1", "GS3": "2", "A3": "3", "AS3": "4", "B3": "5",
"BassDmaj": "6", "BassD": "7", "BassA": "8", "BassAdom7": "9", "BassE": "0"}

class NewPostForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={
        "placeholder": "Title",
        "style": "width: 50%"
    }))
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={
        "placeholder": "Content",
        "style": "width: 50%;"
    }))

class NewLayoutForm(forms.Form):
    changekey = forms.CharField(label="Change", widget=forms.TextInput(attrs={
        "placeholder": "Note",
        "style": "width: 50%"
    }))
    newkey = forms.CharField(label="New", widget=forms.TextInput(attrs={
        "placeholder": "Key On Keyboard",
        "style": "width: 50%"
    }))

# Create your views here.
def index(request):
    newkey = {}
    if request.user.is_authenticated:
        try:
            keyboard = Keyboard.objects.get(changer=request.user)
            for key in keys:
                newkey[key] = getattr(keyboard, key)
        except Keyboard.DoesNotExist:
            keyboard = None
    else:
        newkey = keys
    # VALUES HAVE THE BE UNIQUE CHECK FOR THAT LATER
    newkey = dict((v, k) for k, v in newkey.items())
    newkeyJSON = dumps(newkey)
    print(newkey)
    return render(request, "accordion/index.html", {
        "key": newkeyJSON
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "accordion/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "accordion/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "accordion/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "accordion/register.html", {
                "message": "Username already taken."
            })
        keyboard = Keyboard(changer=user)
        keyboard.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "accordion/register.html")

def forum(request):
    print("*", Post.objects.all().order_by('-timestamp'))
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, "accordion/forum.html", {
        "posts": posts
    })

def demo(request):
    return render(request, "accordion/demo.html")

def share(request):
    return render(request, "accordion/share.html", {
        "form": NewPostForm()
    })

def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            current_user = request.user
            new_post = Post(title=title, content=content, publisher=current_user)
            new_post.save()
        return HttpResponseRedirect(reverse("forum"))
    return render(request, "accordion/index.html", {
        "message": "Accessing new_post view with method that is not post"
    })

def layout(request):
    keyboard = None
    newkey = {}
    if request.user.is_authenticated:
        try:
            keyboard = Keyboard.objects.get(changer=request.user)
            for key in keys:
                note = key
                if (len(key) > 1):
                    if (key[1] == "S"):
                        note = key[0] + "#"
                        if (len(key) > 2):
                            note += key[2]
                newkey[note] = keys[key]
                newkey[note] = getattr(keyboard, key)
        except Keyboard.DoesNotExist:
            pass
    else:
        for key in keys:
            note = key
            if (len(key) > 1):
                if (key[1] == "S"):
                    note = key[0] + "#"
                if (len(key) > 2):
                    note += key[2]
            newkey[note] = keys[key]
    return render(request, "accordion/change.html", {
        "form": NewLayoutForm(),
        "newkey": newkey,
    })

def new_layout(request):
    if request.method == 'POST':
        form = NewLayoutForm(request.POST)
        if form.is_valid():
            
            changekey = form.cleaned_data['changekey']
            tmpkey = ""
            if (len(changekey) > 1):
                if (changekey[1] == "#"):
                    tmpkey = changekey[0] + "S"
                    if (len(changekey) > 2):
                        tmpkey += changekey[2:]
                else:
                    tmpkey = changekey
            else:
                tmpkey = changekey
            changekey = tmpkey
            newkey = form.cleaned_data['newkey']
            current_user = request.user
            # change key is note (C, D, E)
            # new key is keyboard (qwerty)
            # traverse through all attr, if attr value = newkey, set to null
            userkey = Keyboard.objects.get(changer=current_user)
            print(userkey, changekey, newkey)
            for key in keys:
                if (getattr(userkey, key) == newkey): 
                    setattr(userkey, key, "null")
            setattr(userkey, changekey, newkey)
            userkey.save()
        return HttpResponseRedirect(reverse("layout"))
    return render(request, "accordion/index.html", {
        "message": "Accessing new_post view with method that is not post"
    })

def features(request):
    return render(request, "accordion/features.html")