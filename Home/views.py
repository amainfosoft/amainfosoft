from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
import emoji

# Create your views here.

def index(request):
    return render(request,'index.html')

def sending_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        message = name + email + message
        send_mail(subject,message,email,['amainfosoft@gmail.com'],fail_silently=False,)
        reply_msg = 'We have Received your Email Successfully ' + emoji.emojize(":smiling face:")
        messages.add_message(request,messages.success,reply_msg)

        return render(request,'index.html')
    else:
        return render(request,'index.html')


