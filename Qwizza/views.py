from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, "Homepage.html", {})


def discussion(request):
    return render(request, "discussion.html", {})


def signup(request):
    return render(request, "signup.html", {})


def sub_english(request):
    return render(request, "english.html", {})


def sub_math(request):
    return render(request, "Math.html", {})


def sub_physci(request):
    return render(request, "Physicalscience.html", {})


def sub_social(request):
    return render(request, "socialstudies.html", {})


def temp_fib(request):
    return render(request, "FIB.html", {})


def temp_tof(request):
    return render(request, "TrueOrFalse.html", {})


def temp_mcq(request):
    return render(request, "QuestionMCQs.html", {})
