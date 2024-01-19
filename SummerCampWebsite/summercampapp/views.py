from django.contrib import messages
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render
from .models import Program_Management,CityEvent,JobDescription,Feedback,ContactUs

def homepage(request):
    # return HttpResponse("<h1>This is home page</h1>")
    return render(request,'summercampapp/homepage.html')
def program_details(request):
    program_details=Program_Management.objects.all();
    para={
        "programdetails":program_details
    }
    return render(request,'summercampapp/program_management.html',para)

def cityevent(request):
    cityevent=CityEvent.objects.all();
    para={
        "event":cityevent
    }
    return render(request,'summercampapp/city_event.html',para)

def employment_feedback(request):
    employment=JobDescription.objects.all();
    homefeedback = Feedback.objects.all();
    para={
        "job":employment,
        "feed": homefeedback
    }
    return render(request,'summercampapp/homepage.html',para)


def feedback(request):
    if request.method=="POST":
        programname = request.POST.get("pname")
        feedbacktext=request.POST.get("text")
        rating=request.POST.get("rate")
        name=request.POST.get("txtname")
        email=request.POST.get("txtemail")

        if len(name) < 2 or len(email) < 5 or len(programname) < 3 or len(feedbacktext) < 3 or int(rating) >5:
            messages.error(request,"Please fill data properly")
            return render(request, 'summercampapp/feedback.html')

        else:
            feedback = Feedback(Program_name=programname,FeedbackText=feedbacktext,Rating=rating,Name=name, Email=email,Date=timezone.now())
            feedback.save()
            messages.success(request, "Thank You! For Your Feedback.")

    return render(request,'summercampapp/feedback.html')


def about(request):
    return render(request, 'summercampapp/aboutus.html')

def contact(request):
    if request.method == 'POST':
        username = request.POST.get("name")
        email =request.POST.get("txtemail")
        phone=request.POST.get("txtphone")
        question=request.POST.get("ques")
        if len(username) < 2 or len(email) < 5 or len(phone) < 10 or len(question) < 3:
            messages.error(request,"Please fill data properly")
            return render(request, 'summercampapp/contactus.html')

        else:
            contact=ContactUs(UserName=username,Email=email,Phone=phone,Question=question,Date=timezone.now())
            contact.save()
            messages.success(request, "Thank you for contacting us we will reach you shortly")
    return render(request,'summercampapp/contactus.html')

