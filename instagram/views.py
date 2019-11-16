from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import Images, Comments, Profiles
from .forms import PostComment, PostImagesForm, PostProfile

# Create your views here.
@login_required(login_url='/accounts/register/')
def home(request):
    images = Images.get_all_images()
    return render(request,'home.html',{'images':images})


@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = User.objects.get(username=username)
    profile = Profiles.filter_profile_by_id(user.id)
    title = f'{user.username}\'s Profile '
    images = Images.get_profile_images(user.id)
    return render(request, 'profile/profile.html',{'title':title,'users':user,'profile':profile,'images':images})
