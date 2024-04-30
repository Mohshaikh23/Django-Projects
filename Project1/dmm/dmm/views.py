from django.http import HttpResponse

def about_us(request):
    return HttpResponse("Welcome to About Us Page")

def course(request):
    return HttpResponse("Welcome to Course Page")

def coursedetails(request, courseid):
    return HttpResponse(courseid)