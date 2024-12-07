# Django Data Seeding

## Challenge

Seed data is useful for testing and developing an application as it allows us to visualize screens properly with suitable data and develop its functionality effectively. Thankfully, there are a number of tools to make this easy for us with Django.

In this exercise, you will implement Django Seed to populate a Django backend with data for use in the application.

## Key Learnings

- Understanding what seed data is and its importance in development and testing.
- How to set up and use the `django-seed` library to generate dummy data in a Django project.

## User Story

> As a developer, I want to generate realistic seed data for my Django application, so I can properly test and visualize the functionality of my project.

## Acceptance Criteria

1. **Install the Django Seed library**:

   - Use the command `pip install django-seed` to add the library to the project.
   - Alternatively, include the library in the `requirements.txt` file and install it using `pip install -r requirements.txt`.

2. **Add `django_seed` to the project**:

   - Open the `settings.py` file of your Django project.
   - Add `'django_seed'` to the `INSTALLED_APPS` list.
   - set USE_TZ to False

   ```python
   INSTALLED_APPS = [
       # ...
       'django_seed',
   ]

   USE_TZ = False

   ```

3. **Use the seed command to generate data**:

   - Run the seed command to populate your database with dummy data.

   ```bash
   python manage.py seed <your_app_name> --number=<desired_number_of_entries>
   ```

   For this exercise, replace <your_app_name> with courses, and specify the number of entries to generate. Example:

   ```bash
   python manage.py seed courses --number=50
   ```

4. **Verify the generated data**:

- Access your database or the Django admin panel to confirm that the seed data has been added successfully.

Happy coding!
