from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse # Add this
from django.core.mail import send_mail
from .forms import ContactForm # Add this
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request ,'peacebird/home.html',context)    

def enrollment(request):
   
    return render(request ,'peacebird/enrollment.html',)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
          sender_name = form.cleaned_data['name']
          sender_email = form.cleaned_data['email']
          message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
          send_mail('New Enquiry', message, sender_email, ['xafsiina123@gmail.com'])
          return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'peacebird/contact-us.html', {'form': form})




def contact_u(request):

    send_mail('Hello from Hafsa','this test email','xafsiina123@gmail.com',['xafsiina123@gmail.com'],fail_silently=False)

    return render(request, 'peacebird/contact-us.html')

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
