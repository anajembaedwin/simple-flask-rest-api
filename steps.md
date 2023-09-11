## STEPS TO SETUP THE PROJECT
All steps are for Ubuntu (WSL)

1. Install python3-virtualenv:

   ```bash
   sudo apt-get install python3-virtualenv
   ```

2. Create a virtual environment:

   ```bash
   virtualenv venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

4. Install Flask and SQLAlchemy:

   ```bash
   pip install flask
   pip install flask_sqlalchemy
   ```

5. Initialize a Git repository:

   ```bash
   git init
   git branch -m main
   git branch
   touch .gitignore
   git add .
   git commit -m "venv setup complete"
   git remote add origin https://github.com/anajembaedwin/simple-flask-rest-api.git
   git branch -M main
   git push -u origin main
   git remote -v
   ```

6. Install gunicorn:

   ```bash
   pip install gunicorn
   ```

7. Create a Procfile and requirements.txt:

   ```bash
   touch Procfile
   pip freeze > requirements.txt
   touch app.py
   ```

8. Create the database before running the application:
    - Open a Python shell in the virtualenv with `python3`
    - Import the Flask application and database with `from app import app, db`
    - Push an application context with `app.app_context().push()`
    - Import the database and models with `from app import db, Person`
    - Create the tables with `db.create_all()`
    - Exit the Python shell with `exit()`

9. Run the application in development environment with debugging turned on:

    ```bash
    export FLASK_ENV=development
    flask run
    ```

10. Run the application in production environment with debugging turned off:

    ```bash
    export FLASK_ENV=production
    flask run
    ```