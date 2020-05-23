from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import (redirect, render)

from accounts.forms import ProfileEditForm
from accounts.models import Profile


# / -> HOMEPAGE
def home(request):
    return render(request, 'home/index.html')


# / -> PROFILE
@login_required
def profile(request, pk):
    if request.method == 'GET':
        profiled_user = User.objects.get(username=pk)
    context = {'user': profiled_user}
    return render(request, 'profile/profile_detail.html', context)


# / -> DASHBOARD
@login_required
def dashboard(request, pk):
    if request.method == 'GET':
        current_user = User.objects.get(username=pk)
    context = {'user': current_user}
    return render(request, 'dashboard/dashboard.html', context)


# / -> MESSAGES
@login_required
def msg(request, pk):
    if request.method == 'GET':
        current_user = User.objects.get(username=pk)
    context = {'user': current_user}
    return render(request, 'messages/msg.html', context)


# / -> NOTIFICATIONS
@login_required
def notifications(request, pk):
    if request.method == 'GET':
        current_user = User.objects.get(username=pk)
    context = {'user': current_user}
    return render(request, 'notifications/notifications.html', context)


# / -> FAVORITES
@login_required
def favorites(request, pk):
    if request.method == 'GET':
        current_user = User.objects.get(username=pk)
    context = {'user': current_user}
    return render(request, 'favorites/favorites.html', context)


# / -> SEARCH
def search(request):
    return render(request, 'search/search_engine.html')


# / -> LISTING
@login_required
def list_property(request, pk):
    if request.method == 'GET':
        current_user = User.objects.get(username=pk)
    context = {'user': current_user}
    return render(request, 'listing/list_property.html', context)


# / -> AGENCY
def agents(request):
    return render(request, 'agents/find_an_agent.html')


# / -> ADVERTISE
def advertise(request):
    return render(request, 'ads/advertise.html')


# / -> AFFILIATES
def affiliate(request):
    return render(request, 'ads/affiliate_programme.html')


# / -> CAREERS
def careers(request):
    return render(request, 'careers/jobs.html')


# / -> ABOUT US
def about(request):
    return render(request, 'home/about.html')


# / -> FEEDBACK
def feedback(request):
    return render(request, 'home/feedbacks.html')


# / -> LEGAL
def policy(request):
    return render(request, 'legal/privacy_policy.html')


# / -> TERMS & CONDITIONS
def t_and_c(request):
    return render(request, 'legal/t_and_c.html')


# / -> FAQS
def faqs(request):
    return render(request, 'home/faqs.html')
