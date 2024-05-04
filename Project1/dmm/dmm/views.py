from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # data={
    #     'title':"Home Page",
    #     'bdata': "Hello Everyone I hope you are good",
    #     'clist':['PHP', 'Java','Python'],
    #     'numbers': [10,20,30,40,50],
    #     'student_data': [
    #         {'name': 'Mohsin', 'phone': 8999255183},
    #         {'name': 'Harry', 'phone': 9899585252}
    #     ]
    # }
    return render(request, "index2.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")

def blogs(request):
    return render(request, "blogs.html")

def contact(request):
    return render(request, "contact.html")

def course(request):
    return HttpResponse("Welcome to Course Page")

def coursedetails(request, courseid):
    return HttpResponse(courseid)