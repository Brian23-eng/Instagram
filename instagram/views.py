from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import Images, Comments, Profile

# Create your views here.
@login_required(login_url='/accounts/register/')
def home(request):
    return render(request,'home.html')

