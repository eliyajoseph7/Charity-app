from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'hope/pages/index.html')
    
def about_view(request):

    return render(request, 'hope/pages/blog/about.html')    

def blog_view(request):

    return render(request, 'hope/pages/blog/blog.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return HttpResponse("OK")