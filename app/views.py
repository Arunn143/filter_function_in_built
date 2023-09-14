from django.shortcuts import render
import datetime

# Create your views here.

def in_bulit_filter(request):
    data="HIi IAm arUn"
    dt=datetime.datetime.now()
    d={"data":data,'dt':dt}
    return render(request,'in_bulit_filter.html',d)