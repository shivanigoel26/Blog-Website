from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import hashers

# Create your views here.
#home
def home(request):
    return render(request,'blog/home.html')

#about
def about(request):
    return render(request,'blog/about.html')

#contact

def contact(request):

    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Subject = request.POST.get('subject')
        Message = request.POST.get('message')
        data={
            'name':Name,
            'email':Email,
            'subject':Subject,
            'message':Message
        }
        message= ''' 
        New Message: {}

        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message,'' ,['goyalshivani8791@gmail.com'])

    return render(request, 'blog/contact.html', {})


