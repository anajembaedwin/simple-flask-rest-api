All steps are for Ubuntu (WSL)
sudo apt-get install python3-virtualenv
virtualenv venv
source venv/bin/activate
pip install flask
pip install flask_sqlalchemy
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
pip install gunicorn
touch Procfile
pip freeze > requirements.txt
touch app.py
