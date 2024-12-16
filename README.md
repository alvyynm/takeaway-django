# takeaway-django

## Implementation Details
To implement this project, I first decided to create a separate accounts app which handles the different logic and views for login, signup, password reset and password change.

The accounts app is also responsible for displaying the user profile page as the profile is more tied to the user model.

There's also a separate dashboard app whose sole responsibility is to display the dashboard. I took this approach so that the dashboard app can have a clean url (in this case you can access the dashboard at `/` instead of being coupled with the accounts app which has an `accounts/` prefix across all views).

To track the user's last updated data, I use [django-simple-history](https://django-simple-history.readthedocs.io/en/latest/quick_start.html#configure), a third-party package that enables you to track changes to any model instance in django.

## How to run the project
1. Clone the project:
   ```bash
   git clone git@github.com:alvyynm/takeaway-django.git```
2. Navigate to the project directory via the terminal
   ```bash
   cd takeaway-django```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:

   On Windows, run:
   ```bash
   venv\Scripts\activate
   ```
   On Mac OS X, run:

   ```bash
   source venv/bin/activate
   ```
4. Create a `.env` file at the root for email credentials. The required environment variables are listed in `.env.sample`
5. Install project dependencies:
   ```bash
   pip install -r requirements.txt
6. Run migrations:
   ```bash
   python manage.py migrate
   ```
7. Create a superuser (optional -- only if you want to access the admin site):
   ```bash
   python manage.py createsuperuser
   ```
8. Run the project
    ```bash
    python manage.py runserver
    ```
    Open a browser and navigate to http://127.0.0.1:8000/ to view the project.
