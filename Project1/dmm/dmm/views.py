from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

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

def thankyou(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request, "thankyou.html",{'output':output})


def userform(request):
    finals = 0
    data = {}
    try:
        if request.method == "POST":
            print("Request method:", request.method)  # Debugging
            print("Form data:", request.POST)  # Debugging

            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finals = n1 + n2
            data = {
                'n1':n1,
                'n2':n2,
                'output':finals,
            }

            url= "/thankyou/?output={}".format(finals)

            return redirect(url) 
        
    except Exception as e:
        print("Error:", e)  # Debugging

    return render(request, "userform.html", {'output': finals})



def course(request):
    return HttpResponse("Welcome to Course Page")

def coursedetails(request, courseid):
    return HttpResponse(courseid)