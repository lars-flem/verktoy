from django.urls import path
from . import views

app_name="users"

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('profile', views.my_profile, name='my_profile'),
    path('profile/update', views.update_profile, name='update_profile'),
    path('profile/<str:userstring>', views.profile, name='profile'),
]