from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


@login_required
def profile_view(request):
    """Profile view for the authenticated user"""
    return render(request, 'accounts/profile.html')


@login_required
def dashboard_view(request):
    """Dashboard view for the authenticated user"""
    return render(request, 'accounts/dashboard.html')


def signup_view(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
