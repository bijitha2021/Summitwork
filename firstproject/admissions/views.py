from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def addadmission(request):
    values={"name":"Abc","Address":"Texas","phone":"4465454"}
    return render(request,'admissions/add_admissions.html',values)

def addadmissionReports(request):
    return HttpResponse("Reports of  admissions")

