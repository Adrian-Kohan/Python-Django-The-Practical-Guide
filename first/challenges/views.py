from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
 
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for entire month!",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Eat no meat for entire month!",
    "may": "Walk for at least 20 minutes every day",
    "june": "Learn Django for at least 20 minutes every day",
    "july": "Eat no meat for entire month!",
    "august": "Walk for at least 20 minutes every day",
    "september": "Learn Django for at least 20 minutes every day",
    "october": "Learn Django for at least 20 minutes every day",
    "november": "Eat no meat for entire month!",
    "december": "Walk for at least 20 minutes every day",
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})

def monthly_numbers(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirected_month = months[month - 1]
        return HttpResponseRedirect (f"<h1>{redirected_month}</h1>")
    except:
        raise Http404()
    

def challenges(request, month):
    challenge_text = monthly_challenges[month]
    try:
        return render(request, "challenges/challenge.html", {"month":month,
                                                             "challenge": challenge_text})
    except:
        raise Http404()
    
