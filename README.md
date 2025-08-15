# Django Todo Application

A fully functional todo application built with Django that includes user authentication, task management, and a modern responsive UI.

## Features

- ✅ User registration and authentication
- ✅ Create, read, update, and delete tasks
- ✅ Mark tasks as complete/incomplete
- ✅ Responsive Bootstrap UI with Font Awesome icons
- ✅ Task descriptions and timestamps
- ✅ User-specific task management
- ✅ Admin interface for task management

## Setup Instructions

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

4. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

5. **Open your browser and go to:**
   ```
   http://127.0.0.1:8000/
   ```

## Usage

1. **Sign up** for a new account or **login** with existing credentials
2. **Create tasks** using the form on the left side
3. **Edit tasks** by clicking the "Edit" button
4. **Delete tasks** by clicking the "Delete" button
5. **Toggle task status** by clicking the status button (✅/❌)
6. **Logout** using the logout button in the navigation bar

## Project Structure

```
toDo-cursor/
├── toDo/                 # Main project settings
├── task/                 # Task app
│   ├── models.py        # Task model
│   ├── views.py         # View functions
│   ├── urls.py          # URL routing
│   ├── forms.py         # Task forms
│   └── admin.py         # Admin interface
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Main page
│   ├── login.html       # Login form
│   ├── signup.html      # Registration form
│   ├── edit_task.html   # Edit task form
│   └── delete_task.html # Delete confirmation
└── manage.py            # Django management script
```

## Technologies Used

- **Backend:** Django 5.2.4
- **Frontend:** Bootstrap 5.3.1, Font Awesome 6.0.0
- **Database:** SQLite (default)
- **Authentication:** Django built-in user authentication

## Admin Interface

Access the admin interface at `/admin/` to manage users and tasks. You'll need to create a superuser account first.

## Security Features

- CSRF protection on all forms
- User authentication required for task operations
- Users can only access their own tasks
- Secure password handling with Django's built-in validators
