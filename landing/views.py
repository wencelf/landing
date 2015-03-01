from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.mail import EmailMultiAlternatives

def index(request):
    d = str(request.META['HTTP_ACCEPT_LANGUAGE'])
    d = d.replace(';',',')
    d = d.replace('-',',')
    d = d.split(',')
    if d[0] == 'es' or d[0] == 'Es' or d[0] == 'ES' or d[0] == 'eS':
        return render_to_response(
            'esp.html', 
            {},
            context_instance=RequestContext(request)
            )
    elif d[0] == 'en' or d[0] == 'En' or d[0] == 'EN' or d[0] == 'eN':
        return render_to_response(
            'eng.html', 
            {},
            context_instance=RequestContext(request)
            )
    else:
        return render_to_response(
            'eng.html', 
            {},
            context_instance=RequestContext(request)
            )

def sendemail(request):
    if request.method == 'POST':
        subject, to = 'Contact request from the landing page', 'jefrey@startupessentials.co'
        html_content = '<h2>Name</h2><h3>'+request.POST['name']+'</h3><hr><h2>School</h2><h3>'+request.POST['school']+'</h3><hr><h2>Email</h2><h3>'+request.POST['email']+'</h3><hr><h2>Country</h2><h3>'+request.POST['country']+'</h3><hr><h2>Phone number</h2><h3>'+request.POST['phone']+'</h3>'
        msg = EmailMultiAlternatives(subject=subject, to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return HttpResponse('Success')
    else:
        return HttpResponseRedirect('/')