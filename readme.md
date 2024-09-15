# Django Todo List

A simple Todo List web application built with Django. Users can create, update, and delete tasks using a clean and minimal interface.

## Features
- **Add Task**: Users can add new tasks.
- **Edit Task**: Users can edit existing tasks.
- **Delete Task**: Users can delete tasks after confirmation.
- **Mark Task as Complete**: Completed tasks are visually differentiated by strikethrough.

## Requirements

- Python 3.x
- Django 3.x or higher

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/refat-jamil/todo_project.git
cd todo_project 
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Apply Migrations


```bash
python manage.py migrate
```
### 5. Run the Development Server

```bash
python manage.py runserver
```
### 6. Open Your Browser

Visit http://127.0.0.1:8000/ to see the Todo List application in action.

