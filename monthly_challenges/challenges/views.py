from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
#For method 3:

monthly_challenges = {
    'january': "Eat more vegetables every day!",
    'february': "Walk for half an hour every day!",
    'march': "Learn Django for an hour every day!",
    'april': "Read a new book every week!",
    'may': "Take a photo every day!",
    'june': "Write in a journal every day!",
    'july': "Try a new recipe each week!",
    'august': "Go for a run three times a week!",
    'september': "Practice meditation every day!",
    'october': "Learn a new skill!",
    'november': "Volunteer at a local charity!",
    'december': "Reflect on your year and set goals!",
}



# Method 1:
""" def january(request):
    return HttpResponse("Eat more vegetable everyday!")


def february(request):
    return HttpResponse("Walk for half an hours everyday!")

def march (request):
    return HttpResponse("Learn Django for an hour everyday!")
 """


# Method 2:
""" def monthly_challenge_by_number (requst, month):
    return HttpResponse(month)


def monthly_challenge(requst, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat more vegetable everyday!"
    elif month == 'february':
        challenge_text = "Walk for half an hours everyday!"
    elif month == "march":
        challenge_text = "Learn Django for an hour everyday!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text) """
# month here should be exactly the same as what we chose as identifyer in the urls to set it dynamically.

#Method 3:
#To redirect the monthly by number to the dictionalry that we already have:

def monthly_challenge_by_number (requst, month):
    months = list(monthly_challenges.keys())
    
    if month > len (months):
        return HttpResponseNotFound ("invalid month")
    
    redirect_month = months[month - 1]
    return  HttpResponseRedirect ("/challenges/" + redirect_month)

#Retrieve Keys from monthly_challenges: This line creates a list of keys from the monthly_challenges dictionary.
#monthly_challenges.keys() returns a view of the dictionary's keys.
#list() converts this view into a list, so months becomes a list of month names.
#[month - 1] this deduct one from the month, so when we enter 1 we get january instead of feb.


def monthly_challenge(requst, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not found")


