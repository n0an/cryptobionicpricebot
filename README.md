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
