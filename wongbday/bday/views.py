from django.shortcuts import render
import datetime
import pytz


tz = pytz.timezone('Asia/Manila')
now = datetime.datetime.now(tz=tz)
now = str(now)
now = now[5:10]
print(now)


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    if now == "08-07":
        response = "yes"
    else: 
        response = "no"
    return render(request, "greet/response.html",{
        "response": response.capitalize()

    })