# takeaway-django

## Implementation Details

### 1. Authentication
To implement this project, I first decided to create a separate accounts app which handles the different logic and views for login, signup, password reset and password change. This way the authentication logic is separate from the app  for easier maintenance.

The accounts app is also responsible for displaying the user profile page as the profile is more tied to the user model.

To implement, authentication and related functionality, the built-in Django authentication framework with the built-in User model is used for its simplicity.

### 2. Dashboard view
There's also a separate dashboard app whose sole responsibility is to display the dashboard. I took this approach so that the dashboard app can have a clean url (in this case you can access the dashboard at `/` instead of being coupled with the accounts app which has an `accounts/` prefix across all views). This also ensures that if the'res lots of other features needed for the dashboard, it's easier to extend and maintain.

### 3. Tracking a user's last updated details
To track the user's last updated data, I use [django-simple-history](https://django-simple-history.readthedocs.io/en/latest/quick_start.html#configure), a third-party package that enables you to track changes to any model instance in django. It allows tracking of all the changes made to the `User` model in an easy way. For instance, when a user updates their password, the package records when that change was made.

While Django has a feature that tracks changes to any model instance in the admin interface, it doesn't track changes made to models outside of it. For this reason, using a third-party package like `django-simple-history` made more sense.

### NOTE:
In order to send a password reset email, make sure your ISP is not blocking port 587. If password reset emails are blocked (if you see a `TimeoutError: timed out` error), you can hotspot your device using your phone/tablet and test the feature again.

For linting, flake8 is used (for Python code) and djlint for linting django templates. I've also setup a precommit hook to ensure linting rules are respected before a commit is accepted.

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
