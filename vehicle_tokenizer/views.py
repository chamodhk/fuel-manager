import imp
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages

from .models import Vehicle
# Create your views here.

def check_vehicle(request):
    reg_number = "".join(request.GET['reg'].split())
    vehicle = Vehicle.objects.filter(reg_number=reg_number)
    if vehicle.exists():
        vehicle = vehicle[0]
        available = vehicle.type.quota - vehicle.usage
        context = {
            'registered': True,
            'reg': vehicle.reg_number,
            'available': available,
            'quota': vehicle.type.quota,
            'percentage': round(vehicle.usage/vehicle.type.quota*100),
        }
        
    else:
        context= {
            'registered': False,
        }
        
    return render(request,'html/pump.html',context)
def welcome(request):
    return render(request,'html/main.html')

def update(request):
    pumped_amount = int(request.POST['number'])
    reg = request.POST['reg_number']
    vehicle = Vehicle.objects.filter(reg_number = reg)[0]

    vehicle.usage = vehicle.usage + pumped_amount
    vehicle.save()

  
    messages.success(request,"Details updated succesfully")

    return HttpResponseRedirect('/welcome/')
    