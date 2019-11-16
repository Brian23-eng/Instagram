from django.shortcuts import render, redirect
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


@login_required(login_url='/accounts/login/')
def post_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostImagesForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
            return redirect('profile',username=request.user)
    else:
        form = PostImagesForm()
    return render(request,'profile/post_image.html',{'form':form})
