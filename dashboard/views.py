from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def dashboard_view(request):
    """Dashboard view for the authenticated user"""
    return render(request, 'dashboard/dashboard.html')
