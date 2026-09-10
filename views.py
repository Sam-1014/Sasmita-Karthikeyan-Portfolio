from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, ContactMessage

def home(request):
    projects = Project.objects.all().order_by('-created_at')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')

    return render(request, 'portfolio/index.html', {'projects': projects})