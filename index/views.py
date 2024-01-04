from django.shortcuts import render, redirect,get_list_or_404, get_object_or_404
from .models import *
# from .forms import *
from django.contrib import messages
from django.http import HttpResponse, request
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import EmailMessage,EmailMultiAlternatives




def myindex(request):
    qs1 = About.objects.all()
    trend = Blog.objects.filter(trending=True)
    featured_obj = Blog.objects.all().filter(featured=True).order_by('-created_at')[:5]
    post_obj = Blog.objects.all().filter(status='active', visible=True,featured=False).order_by('-created_at')[:1]
    qs = Blog.objects.filter(status='active').order_by('-created_at')[:10]
    ew = Blog.objects.filter(video=True)[:10]
    gf = Catagory.objects.filter()[:6]
    sax = ads.objects.all()
    context = {'post':post_obj,'por':qs1}
    return render(request, 'index/index.html',context)
    
def mycontact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('msg')
        cre = Contact.objects.create(name=name,email=email,subject=subject,message=message)
        msg = EmailMessage(
        'contact request',
        cre.name + " Has contacted you . " + cre.email + " , check your dashboard for more info",
        settings.DEFAULT_FROM_EMAIL,
        ['obnoxiouscasio@gmail.com'],
        )
        msg.send()
        messages.success(request, 'We will get back to you shortly')
    return render(request, 'index/contact.html')

def myrat(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    trend = Blog.objects.filter(trending=True)
    sax = ads.objects.all()
    blog = post.comments.filter()
    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        try:
            user = User.objects.get(username=request.user)
            cra = Comment.objects.create(name=name,body=body,post=post)
        except post.DoesNotExist:
            messages.success(request, 'waka...$and login')
    else:
        messages.success(request, '')
    context = {'data':post,'num':trend, 'comments':blog,'ads':sax}
    return render(request, 'index/post-1.html',context)

def myall(request):
    qs = Blog.objects.all()
    trend = Blog.objects.filter(trending=True)
    context = {'num':trend,'qs':qs}
    return render(request, 'index/all.html',context)


def myabout(request):
    qs = About.objects.all()
    context = {'qs':qs}
    return render(request, 'index/about-us.html',context)
