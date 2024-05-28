from django.urls import path
from . import views


#Method 1
""" urlpatterns = [
    path('january/', views.january),
    path('february/', views.february),
    path('march/', views.february),
] """

#Method 2.   Setting the value dynamically.
urlpatterns = [
    path("", views.index, name="index"),    #empty because this is sent to the /challenges/ in main url
    path('<int:month>/', views.monthly_challenge_by_number),
    path('<str:month>/', views.monthly_challenge, name="month-challenge"),
]
#<> : django placeholder syntax.   in between any identifyer of my choice. 
# and we put that as an argument in in views.py
#str: is path converter. this tells django that the concere value entered here should be treated as a string. (that means if i press 1, it should be treated/ converted to january)
 
