from re import template
from django.shortcuts import redirect, render
from .forms import LaptopForm
from.models import Laptop

# Create your views here.
def LaptopView(request):
    form = LaptopForm()
    template_name = 'crudapp/lapform.html'
    
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, template_name, context)

def showLaptop(request):
    data = Laptop.objects.all()
    template_name ='crudapp/showlap.html'
    context = {'obj':data}
    return render(request, template_name, context)

def updateLaptop(request,id):
    data = Laptop.objects.get(laptop_id = id)
    form = LaptopForm(instance=data)
    template_name = 'crudapp/lapform.html'
    context = {'form':form}
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=data)
        form.is_valid()
        form.save()
        return redirect('showlaptop_url')
    return render(request, template_name, context)

def deleteLaptop(request, id):
    data = Laptop.objects.get(laptop_id = id)
    template_name = 'crudapp/delconfirm.html'
    context = {'obj':data}
    if request.method == 'POST':
        data.delete()
        return redirect('showlaptop_url')
    return render(request, template_name, context)

