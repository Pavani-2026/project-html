from django.shortcuts import render
from productapp.models import productInvoice
from productapp.forms import productInvoiceForm

# Create your views here.
def insert_product(request):
    if request.method=="POST":
        form=productInvoiceForm(request.POST)
        if form.is_valid():
            pid=form.cleaned_data('pid'),
            name=form.cleaned_data('name'),
            price=form.cleaned_data('price'),
            quantity=form.cleaned_data('quantity'),
            total=form.cleaned_data('total'),
            total=price*quantity;
            discount=0.0
            if(total<5000):
                discount=(total*15)/100
            elif(total>5000):
                discount=(total*21)/100
            elif(total<20000):
                discount=(total*31)/100
            elif(total>20000):
                discount=(total*41)/100
                
