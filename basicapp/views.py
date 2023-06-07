from django.shortcuts import render
from basicapp.models import *
from basicapp.forms import BookingForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def furnitureitems(request):
    furniture_items = FurnitureItems.objects.all()
    furniture_itemslist = {"furnitureitemName": furniture_items}
    return render(request, 'furnitureitems.html', {"furnitureitemName": furniture_itemslist})



def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html',context)


def modularItems(request): 
    modular_items=ModularItem.objects.all()
    modular_itemslist={"modularitem":modular_items}
    return render(request, 'modularitem.html',{'modularitemms':modular_itemslist}) 

def chaukos(request): 
    chaukos_category=Chaukos.objects.all()
    chaukos_itemslist={"chaukos":chaukos_category}
    return render(request, 'chaukosdetails.html',{'chaukos':chaukos_itemslist}) 
