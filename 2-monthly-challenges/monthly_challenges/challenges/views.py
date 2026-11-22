from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 30 minutes every day!",
    "march": "Learn Django for 20 minutes every day!",
    "april": "Learn scuba diving for 20 minutes every day!",
    "may": "Travel to a new country and learn about its culture.",
    "june": "Read a new book every week.",
    "july": "Take a photography class and capture beautiful moments.",
    "august": "Volunteer for a local charity or community organization.",
    "september": "Start a new hobby or learn a new skill.",
    "october": "Write a daily journal or blog about your experiences.",
    "november": "Practice mindfulness and meditation for 10 minutes every day.",
    "december": "Reflect on the year and set goals for the next year."
}

# Create your views here.
def index(request):
    list_items = ["<ul>"]
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months" : months
    })
def january(request):
    return HttpResponse("This works successfully!")
def february(request):
    return HttpResponse("This is the feburary challenge for you!")

def march(request):
    return HttpResponse("Learn Django for 20 minutes everyday.")

# def monthly_challenge(request, month):
#     challenge_text = monthly_challenges.get(month)
#     if challenge_text is None:
#         return HttpResponseNotFound("<h1>This month is not supported!</h1>")
#     response_data = f"<h1>{challenge_text}</h1>"
#     return HttpResponse(response_data)

def monthly_challenge(request, month):
    challenge_text = monthly_challenges.get(month)
    if challenge_text is None:
        raise Http404() # this will automatically search for a 404.html file in the templates folder and render it. If we don't have a 404.html file, it will show the default 404 page.
    return render(request,"challenges/challenge.html", { # Third argument is a dictionary that we can use to pass data to the template. The keys of the dictionary are the names of the variables that we want to use in the template and the values are the values of those variables. In this case, we are passing the challenge_text variable to the template and we can use it in the template as {{ text }}. We are also passing the month variable to the template and we can use it in the template as {{ month_name }}.
        "text" : challenge_text,
        "month_name" : month.capitalize()
    }) # request here is required and the second argumemt is the path to the file
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    redirect_month = months[month - 1]
    reverse_url = reverse("month-challenge", args = [redirect_month]) # reverse() function takes in the name of the url pattern and returns the url pattern as a string. It also takes in the args parameter which is a list of arguments that we want to pass to the url pattern. In this case, we are passing the redirect_month variable as an argument to the url pattern.
    return HttpResponseRedirect(reverse_url) # we redirect to this url; it's as if the user typed this url in the browser.



