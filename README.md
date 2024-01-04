# User Authentication with Email OR Username in Django

This is a simple Django web application that provides user authentication using both username and email.
#### Deployment - [auth.harshp.in](auth.harshp.in)

## Table of Contents

- [Objective](#objective)
- [Requirements](#requirements)
- [Additional Notes](#additional-notes)
- [Submission](#submission)
- [Setup and Run](#setup-and-run)
- [Project Walkthrough Video](#project-walkthrough-video)

## Objective

Create a Django web application with user authentication features, including user registration, login, basic user profile, and logout.

## Requirements

- [x] Use Django to create a new project and a single app. 
- [x] Implement a user registration (sign-up) page with the following fields:
   - Username
   - Email
   - Password
   - Confirm Password
- [x] Implement a user login page with the following fields: 
   - Username or Email
   - Password
- [x] After successful login, redirect the user to a simple dashboard page that displays a welcome message with their username.
- [x] Implement a basic user profile page that displays user information. Users should only be able to access this page if they are logged in.
- [x] Implement a logout functionality that logs the user out and redirects them to the login page.
- [x] Use Django's built-in authentication system for handling user registration, login, and logout.

### Additional Notes

- [x] Ensure the password is securely stored using Django's password hashing.
- [x] Implement proper form validation to handle errors during registration and login.
- [x] Use Django templates for rendering HTML pages.
- [x] Apply basic styling using CSS (you can use an external library like Bootstrap if you prefer).
- [x] Create a simple SQLite database to store user information.

## New Features Implemented

- [x] Implemented Forgot Password and Change Password Features using features provided in the Django Contrib.
- [x] Implemented SMTP Email Backend to send an email for Forgot Password.
- [x] Deployed the project to [auth.harshp.in](auth.harshp.in) with a PostgreSQL database using the deployment branch.
  
## Setup and Run

0. (Optional) Activate a virtual environment to isolate dependencies.

```bash
pip install virtualenv
python -m virtualenv venv
venv/Scripts/activate (Windows)
source venv/bin/activate (Linux)
```

1. Clone the repository:

```bash
git clone https://github.com/yourusername/django-user-authentication.git
cd django-user-authentication
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply Migrations:

```bash
python manage.py migrate
```

4. Run the development server:

```bash
python manage.py runserver
```

5. Visit [localhost:8000](https://localhost:8000) in browser to access the application.

6. ## Project Walkthrough Video
[Link to the video](auth.harshp.in)
