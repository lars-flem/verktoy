from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib import messages
from django.views import generic
from homepage.models import Listing, Agreement
from homepage.models import UserDefinedList
from .forms import MakeFavouritesListForm

# Create your views here.

#https://docs.djangoproject.com/en/4.1/topics/auth/default/#how-to-log-a-user-in
#https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

#Henter siden for å registrere ny bruker
def signup(request):
    if request.method == 'POST': #når man sender skjema
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1') #hashet passord
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
        else:
            print("Invalid form")
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = UserCreationForm #når man laster inn login siden først
    return render(request, 'users/signup.html', {'form': form})

#Henter min profil-siden
@login_required
def my_profile(request):
    current_user = request.user
    user_listings = current_user.listing_set.all()
    user_profile = current_user.profile
    listings = []

    if request.POST.get('loaned_out'):
        for listing in user_listings:
            if listing.loaned:
                listings.append(listing)
    
    elif request.POST.get('my_loans'):
        agreements= Agreement.objects.filter(loaner=request.user)
        for agreement in agreements:
            listings.append(agreement.listing)
        #listings = agreements.objects.agreement_listing.all()
    else:
        for listing in user_listings:
            if not listing.loaned:
                listings.append(listing)
                
    mine_favoritter = current_user.list_owner.all()
    form = MakeFavouritesListForm(request.POST)
    allListings = Listing.objects.all()
    if form.is_valid():
        newList = form.save(commit=False)
        newList.owner = current_user
        newList.save()        
    else:
        form = MakeFavouritesListForm()
    context = {'user': current_user, 'listings': listings, 'profile': user_profile, 'mine_favoritter':mine_favoritter, 'form':form, 'allListings': allListings}
    return render(request, 'users/my_profile.html', context)

@login_required
def profile(request, userstring):
    requested_user = User.objects.get(username = userstring)
    user_listings = requested_user.listing_set.all()
    user_profile = requested_user.profile

    context = {'user': requested_user, 'listings': user_listings, 'profile': user_profile}
    return render(request, 'users/profile.html', context)


#henter siden for å oppdatere profil. Bruker ProfileForm definert i forms.py
@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profilen din ble oppdatert')
            return redirect('users:my_profile')
        
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    context = {'profile_form': profile_form}
    return render(request, 'users/update_profile.html', context)

