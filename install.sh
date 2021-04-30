#!/bin/sh

# activate venv
source bin/activate
# install dependencies
pip install -r requirements.txt
# Google authentication
python3 google_auth.py