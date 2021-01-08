from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Portfolio

# Create your views here.
def index(request):
    portfolios = Portfolio.objects.all().order_by('-id')[:9]
    return render(request, 'hope/pages/index.html', {'portfolios': portfolios})
    
def about_view(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'hope/pages/blog/about.html', {'portfolio':portfolio})    

def blog_view(request, slug):
    portfolio = Portfolio.objects.get(slug=slug)
    related = Portfolio.objects.exclude(slug=slug)[:4]
    return render(request, 'hope/pages/blog/blog.html', {'portfolio': portfolio, 'related': related})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return HttpResponse("OK")


def portfolio_view(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'hope/pages/blog/allPortfolios.html', {'portfolio': portfolio})        


def about_me(request):
    return render(request, 'hope/pages/aboutMe.html')
    

def donation_view(request):

    return render(request, 'hope/pages/donation.html')    

