from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .models import *
from .forms import *
from msc.settings import MEDIA_URL,MEDIA_ROOT
from django.contrib.auth import logout
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


User = get_user_model()
def home(request):
    team=Secretarie.objects.all()
    about=About_us.objects.all()
    events=Events.objects.all()
    post=Post.objects.all().order_by('-timestamp')
    Gallery_Img=index_gallery.objects.all()
    about_us_content=About_us_content.objects.all()
    context={
    "core_team":team,
    "about_us_content":about_us_content,
    "abt":about,
    "evnt":events,
    "post" : post,
    "gall_img":Gallery_Img,
    }
    return render(request, 'src/index.html',context)

def logout_view(request):
    logout(request)
    template = 'src/index.html'
    return render(request, template)

def team_page(request):
    technical=Team.objects.filter(department='1st')
    event_management=Team.objects.filter(department='2nd')
    creativity=Team.objects.filter(department='3rd')
    publicity=Team.objects.filter(department='4th')
    context = {
    "technical": technical,
    "event_management":event_management,
    "creativity":creativity,
    "publicity":publicity,
    }

    return render(request,'src/about_us.html',context)


def main_gallery(request):
    title= ": Gallery"
    msweek=MSWEEK_gallery.objects.all()
    inspirus=INSPIRUSUS_gallery.objects.all()
    rumble=RUMBLE_gallery.objects.all()
    context = {
    "title": title,
    "msweek":msweek,
    "inspirus":inspirus,
    "rumble":rumble,
    }

    return render(request, 'src/full_gallery.html',context)

def newsfeed(request):
    post=Post.objects.all()
    context= {
    "post":post,
    }

    return render(request,'src/newsfeed.html',context)


class DetailView(generic.DetailView):
    model=Post
    template_name = 'src/detail.html'

def msweek_event(request):
    title = "MS Week"
    events=MSWeek_Event.objects.all()
    context = {
    "title":title,
    "events":events
    }

    if(events):
        return render(request, 'src/events.html', context)
    else:
        return render(request, 'src/events_soon.html', context)

def inspirus_event(request):
    title = "INSPIRUS"
    events=Inspirus_Event.objects.all()
    context = {
    "title":title,
    "events":events
    }
    if(events):
        return render(request, 'src/events.html', context)
    else:
        return render(request, 'src/events_soon.html', context)

def rumble_event(request):
    title = "RUMBLE"
    events=Rumble_Event.objects.all()
    context = {
    "title":title,
    "events":events
    }

    if(events):
        return render(request, 'src/events.html', context)
    else:
        return render(request, 'src/events_soon.html', context)

def ContactView(request):
    title= ": Contact"
    context={
    "title":title,
    }

    return render(request,'src/contact3.html',context)    
