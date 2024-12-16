from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
]
