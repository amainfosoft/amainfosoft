from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
import emoji

# Create your views here.

def index(request):
    return render(request,'index.html')

def sending_email(request):
    susmsg = []
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        message = name +' '+ email+' ' + message
        send_mail(subject,message,email,['amainfosoft@gmail.com'],fail_silently=False,)
        #reply_msg = 'We have Received your Email Successfully ' + emoji.emojize(":smiling face:")
        #messages.add_message(request,messages.success,'We have Received your Email successfully...')
        susmsg = 'We have Received your Email Successfully, We will get back to you soon.'
        #susmsg.append(msg)

        #return render(request,'index.html',{'susmsg':susmsg})
        return redirect('index',{'susmsg':susmsg})
    else:
        return render(request,'index.html')


