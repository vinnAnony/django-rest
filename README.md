# Create a python environment
python -m venv venv

# Activate the environment
source ./venv/Scripts/activate

# Install required packages
pip install -r requirements.txt

# Running Server
python manage.py runserver 8000