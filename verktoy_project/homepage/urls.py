from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="homepage"

urlpatterns = [
    path('home/', views.home, name='home'), #placeholder?
    path('landingpage/', views.landingpage, name='landingpage'),
    path('listing/<int:listing_id>', views.listing, name='listing'),
    path('listing/add/', views.add_listing, name='add_listing'),
    path('listing/overview', views.listing_overview, name='listing_overview'),
    path('listing/edit/<int:listing_id>', views.edit_listing, name='edit_listing'),
    path('listing/remove/<int:listing_id>', views.remove_listing, name='remove_listing'),
]