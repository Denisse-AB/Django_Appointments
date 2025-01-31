# Django Appointments

Single Page Application (SPA) to make appointments using Vue 3 composition API, Django, and Django Rest Framework.

## Requirements

Vue 3 | Python ^3.9.4 | PostgreSQL

## Description

This application consists of a form in which your clients or users are going to make appointments for your business or organization. The user will receive an email when the appointment is accepted.

The owner of this application will manage these appointments through Django Admin. It is configured to receive four appointments every hour (You can change this in the views.py file), it has English and Spanish translation and the database it uses is Postgressql, you can configure it however you want 👍

## Demo

frontend Demo
[Appointment Form](https://denisse-ab.github.io/app-pages-v2/)

## Setup Django Development

- [Fork the repository](https://docs.github.com/es/get-started/quickstart/fork-a-repo).
- Create a new directory
- cd to your new directory

- Create a virtual environment
  - [Instructions to create the .env](https://docs.djangoproject.com/en/3.2/howto/windows/#setting-up-a-virtual-environment/).
  - [Virtual Environment](https://docs.python.org/3/tutorial/venv.html).

- Activate the virtual environment

- Clone repository (make sure your environment is Activated)

<!-- TODO: CHECK NAME OF APP -->
```bash
git clone https://github.com/your-user-name/Django_Appointments.git
```

- cd to Django_Appointments
- install the requirements.txt

```python
cd Django_Appointments
pip install -r requirements.txt
```

- Change the SECRET_KEY and variables in the settings.py file
- Connect your database in setting.py
- Run the migrations
- Create superuser

```python
# Mac and Linux use Python instead of py
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

## Setup Vue Development

```javascript
cd frontend
npm install
npm run serve
```
---

<p align="center">
  <img src="screenshots\screenshot(1).png" width="450" alt="app form">
  <img src="screenshots\screenshot(2).png" width="450" alt="app form">
  <img src="screenshots\django-admin.png" width="450" alt="django admin">
</p>

---
