from django.urls import path
from . import views

# urlsPatterns is a list of all the urls that we want to register for this app
# path is a function that takes in two arguments, the first argument is the url pattern and the second argument is the view function that we want to call when this url pattern is matched
# The function that we are calling must be imported in the top file of this file as you can see in the case of from . import views

# <> is a placeholder for a variable that we want to pass to the view function. In this case,
# whatever the user passes after /challenges/ will be passed to the monthly_challenge view function as a variable called month
urlpatterns = [
    path("january", views.january),
    path("february", views.february),
    path("march", views.march),
    path("", views.index, name="index"), # this is the home page
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge,name = "month-challenge") # str: means we are treating the variable as a string. We can also use int: if we want to treat the variable as an integer
]