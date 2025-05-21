# Task Tracker

A Django web application for managing personal tasks with priority levels and completion tracking.

# Task Tracker Screenshot

### Homepage:

<img src="https://github.com/user-attachments/assets/5c01604c-a7ae-4dd2-9444-b45da254c797" width="600"/>


### Add Task:

<img src="https://github.com/user-attachments/assets/e210a42c-af14-4f4f-b4d2-6ed3c4918d8a" width="600"/>


## Features



## Features

- Create tasks with title, description, and priority level (Low, Medium, High)
- Visual priority indication with color-coding
- Track task completion status
- Simple and intuitive user interface

## Technology Stack

- Django 5.2
- Python 3.13
- HTML/CSS
- SQLite database

## Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/prithveerarya345/django-task-tracker.git
   cd django-task-tracker
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install django
   ```

4. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- **View Tasks**: The home page displays all active and completed tasks
- **Add Tasks**: Click "Add New Task" to create a new task with priority level
- **Complete Tasks**: Click the "Complete" button on any task to mark it as completed

## Project Structure

```
task_tracker/
├── manage.py
├── task_tracker/          
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tasks/                
    ├── admin.py           
    ├── forms.py 
    ├── models.py          
    ├── templates/         
    │   └── tasks/
    │       ├── add_task.html
    │       ├── base.html
    │       └── task_list.html
    ├── urls.py            
    └── views.py           
```

## Todo: 

- User authentication and personal task lists
- Due dates and reminders
- Task categories and filtering
- Task search functionality
- Task editing

