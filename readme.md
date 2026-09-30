# My Django API Project

This is a REST API built with Django and Django REST Framework.

### Prerequisites

Make sure you have Python 3.10+ and Git installed on your system.

## Features
- Nested serialization Implementation in blog app
- Employee tracking and filtering
- Custom pagination rules
- CRUD operations

1. Cloning the Repository

```bash
# Clone the repository
git clone https://github.com/Yashvant05/restapilearning.git
```

2. Setting Up the Virtual Environment
```bash
# Create a virtual environment named .venv
python -m venv .venv

# Activate the virtual environment
# On Windows (Command Prompt):
.venv\Scripts\activate

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

# On macOS/Linux:
source .venv/bin/activate
```

3. Installing Dependencies
```bash
pip install -r requirements.txt
```

4. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Running the Application
Start the local development server:

```bash
python manage.py runserver
```

Once the server starts, open your browser or API client (like Postman or ThunderClient in VS Code) and navigate to:
* **Base API Endpoint:** `http://127.0.0`