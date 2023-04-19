from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

def student(request):
    SFO=StudentForms()
    d={'SFO':SFO}
    if request.method=='POST':
        FD=StudentForms(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'student.html',d)
