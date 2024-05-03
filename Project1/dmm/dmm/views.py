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


def generic(request):
    return render(request, "generic.html")

def elements(request):
    return render(request, "elements.html")


def about_us(request):
    return HttpResponse("Welcome to About Us Page")

def course(request):
    return HttpResponse("Welcome to Course Page")

def coursedetails(request, courseid):
    return HttpResponse(courseid)