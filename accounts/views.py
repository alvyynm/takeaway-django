from django.shortcuts import render

# Create your views here.


def profile_view(request):
    """Profile view for the authenticated user"""
    return render(request, 'accounts/profile.html')
