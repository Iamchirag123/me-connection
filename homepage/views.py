from django.shortcuts import render
from .models import company, user, socialmedia

# Create your views here.
def index(request, slug):
    data = {}

    userdata = user.objects.get(slug = slug)
    sociallink = socialmedia.objects.filter(company = userdata.company)
    data['data'] = userdata
    data['sociallink'] = sociallink

    return render(request,  'homepage.html' , data)