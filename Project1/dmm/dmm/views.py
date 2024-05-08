from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import userForm

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
        n = eval(request.POST.get("num1"))
        if n%2==0:
            c = "Even"
        else:
            c = "Odd"
    return render(request, "evenodd.html", {'c':c})