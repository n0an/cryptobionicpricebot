On localhost:
```
python3 -m venv venv
source venv/bin/activate
mkdir app & cd app
pip install -r requirements.txt
python main.py
```

On pythonanywhere.com:
```
virtualenv venv --python=python3.6
source venv/bin/activate
pip install flask
pip install flask-sslify
pip install requests
```

Deploy ways:
1. localhost.run
2. ngrok.com
3. pythonanywhere

Pythonanywhere deployment:
1. Create and activate venv in cli
2. Install requirements using pip
3. Upload files to /home/username/bot folder
4. Web tab: Add new web app (with manual configuration)
    - specify source code dir: /home/username/bot
    - specify venv path: /home/username/venv
    - edit noant_pythonanywhere_com_wsgi.py - use file in this repo
