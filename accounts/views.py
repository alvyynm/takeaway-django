from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
# Create your views here.


@login_required
def profile_view(request):
    """Profile view for the authenticated user"""
    user_history = request.user.history.all().order_by('-history_date')

    context = {
        'user': request.user,
        'last_updated': user_history.first().history_date if user_history.exists() else None
    }
    return render(request, 'accounts/profile.html', context)


def signup_view(request):
    """User registration view"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
