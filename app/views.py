from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def create_scl(request):
    SEEFO=schoolForm()
    d={'SEEFO':SEEFO}
    if request.method=='POST':
        SEFO=schoolForm(request.POST)
        if SEFO.is_valid():
            sn=SEFO.cleaned_data['Sname']
            sp=SEFO.cleaned_data['Sprinc']
            sl=SEFO.cleaned_data['Sloc']
            SO=school.objects.get_or_create(Sname=sn,Sprinc=sp,Sloc=sl)[0]
            SO.save()
            return HttpResponse('school is created')
        else:
            return HttpResponse('invalid data')
    return render(request,'create_scl.html',d)

