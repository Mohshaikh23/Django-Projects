import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import userForm
import math
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from contactenquiry.models import enquiry
from django.core.mail import send_mail
from django.conf import settings



def homepage(request):
    # subject = "Testing Mail",
    # message = "Here is the message.",
    # email_from = "mohsin.shaikh324@gmail.com",
    # recipient_list = ["mohsin.shaikh23951@gmail.com"],
    # fail_silently=False
    
    # send_mail(subject, message, email_from, recipient_list)

    return render(request, "index2.html")


def about(request):
    return render(request, "about.html")


def services(request):
    servicesData = Service.objects.all()
    
    if request.method == "GET":
        st = request.GET.get('service_name')
        if st!= None:
            servicesData = Service.objects.filter(service_title__icontains=st)
    data = {
        'servicesData':servicesData
    }
    return render(request, "services.html", data)

def blogs(request):
    blogdata = News.objects.all()
    blog_data = {
        "BlogsData":blogdata
    }
    return render(request, "blogs.html", blog_data)

def contact(request):
    return render(request, "contact.html")

def submit_enquiry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = enquiry(e_name=name, 
                       e_email = email,
                       e_message=message)
        data.save()
    return render(request, "contact.html")


def userform(request):
    finals = 0

    fn = userForm()
    
    data = {'form':fn}
    try:
        if request.method == "POST":
            print("Request method:", request.method)  # Debugging
            print("Form data:", request.POST)  # Debugging

            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finals = n1 + n2
            data = {
                'form':fn,
                'output':finals,
            }

            url= "/thankyou/?output={}".format(finals)

            return HttpResponseRedirect(url) 
        
    except Exception as e:
        print("Error:", e)  # Debugging

    return render(request, "userform.html", data)

def thankyou(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request, "thankyou.html", {'output': output})

def course(request):
    return HttpResponse("Welcome to Course Page")

def coursedetails(request, courseid):
    return HttpResponse(courseid)

def calculator(request):
    c = ""
    try:
        if request.method=="POST":
            num1 = eval(request.POST.get("num1"))
            num2 = eval(request.POST.get("num2"))
            opr = request.POST.get("OPR")

            if opr == "+":
                c = num1 + num2
            elif opr == "-":
                c = num1 - num2
            elif opr == "/":
                c = num1 / num2
            elif opr == "*":
                c = num1 * num2

    except Exception as e:
        print(e)
    
    print(c)
    return render(request, "calculator.html", {"c":c})

def even_odd(request):
    c = ""
    if request.method == "POST":
        if request.POST.get('num1') == "":
            return render(request, "evenodd.html", {'error':True})
        
        n = eval(request.POST.get("num1"))
        if n%2==0:
            c = "Even"
        else:
            c = "Odd"
    return render(request, "evenodd.html", {'c':c})

def marksheet(request):
    if request.method == "POST":
        s1 = eval(request.POST.get('subject1'))
        s2 = eval(request.POST.get('subject2'))
        s3 = eval(request.POST.get('subject3'))
        s4 = eval(request.POST.get('subject4'))
        s5 = eval(request.POST.get('subject5'))
        t = s1+s2+s3+s4+s5
        p = t*100/500
        if p>60:
            d = "First Division"
        elif p>=48:
            d = "Second Division"
        else:
            d = "Third Division"
        data = {'total':t, 
                'percentage':math.floor(p),
                'division':d}
        return render(request, "marksheet.html", data)
    return render(request, "marksheet.html")

def blogview(request, slug):
    blog = News.objects.get(news_slug = slug)
    blog_data = {
        'blog': blog
    }
    return render(request, "blogview.html", blog_data)