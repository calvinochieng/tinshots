from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .models import *
from .forms import *

def index(request): 
    portfolios = Portfolio.objects.all().order_by('order')
    form = BookingForm() 
    contact_form = ContactForm()
    return render(request, 'index.html', {'portfolios': portfolios, 'form': form, 'contact_form': contact_form})
def home(request):
    portfolios = Portfolio.objects.all().order_by('order')
    form = BookingForm() 
    contact_form = ContactForm()
    return render(request, 'home.html', {'portfolios': portfolios, 'form': form, 'contact_form': contact_form})

def portfolio(request,pkid=None):   
    items = PortfolioImage.objects.all()
    return render(request, 'list.html', {'items': items})

def portfolio_detail_view(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    images = PortfolioImage.objects.filter( portfolio =  portfolio)
    form = BookingForm()
    return render(request, 'detail.html', {'portfolio': portfolio, 'form': form, 'images' : images})


def gallery_view(request):
    images_list = PortfolioImage.objects.all().order_by('id')
    paginator = Paginator(images_list, 20)  # Show 20 images per page

    # Get the current page number from the query parameters
    page_number = request.GET.get('page')
    images = paginator.get_page(page_number)

    form = BookingForm()
    return render(request, 'gallery.html', {'images': images, 'form': form})


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

def pricing(request):
    return render(request, 'pricing.html')

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
