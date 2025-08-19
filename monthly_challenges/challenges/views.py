from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
month_challenge_dict = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

def months_list():
    return list(month_challenge_dict.keys())

def index(request):
    return render(request, 'challenges/index.html', {
        'months': months_list()
    })    

def month_view(request, month):

    try: 
        challenge_text = month_challenge_dict[month]
        return render(request,'challenges/challenge.html', {
            'text' : challenge_text,
            'month_name': month,
        })
    except:
        raise Http404("This month is not supported")
    
def month_view_int(request, month):
    
    months = months_list()
    redirect_month = months[month - 1]

    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path) 


    