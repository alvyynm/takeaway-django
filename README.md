# takeaway-django

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
7. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
8. Run the project
    ```bash
    python manage.py runserver
    ```
    Open a browser and navigate to http://127.0.0.1:8000/ to view the project.
