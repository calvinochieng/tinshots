from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages

from .models import *
from .forms import *

def index(request): 
    portfolios = Portfolio.objects.all()
    form = BookingForm() 
    contact_form = ContactForm()
    return render(request, 'index.html', {'portfolios': portfolios, 'form': form, 'contact_form': contact_form})

def portfolio(request,pkid=None):   
    items = PortfolioImage.objects.all()
    return render(request, 'list.html', {'items': items})

def portfolio_detail_view(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    images = PortfolioImage.objects.filter( portfolio =  portfolio)
    form = BookingForm()
    return render(request, 'detail.html', {'portfolio': portfolio, 'form': form, 'images' : images})


def gallery_view(request):
    images = PortfolioImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been successfully submitted, we'll get back to you ASAP!")
            return redirect('/')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})

def terms(request): 
    return render(request, 'terms.html')



def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!") 
    else:
        form = ContactForm()
    return redirect('/')
