from django.contrib.auth.models import User

from simple_history import register

# register the default User model for history tracking
register(User)
