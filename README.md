# blog

testing Jenkins 1
A blog and personal site for Ben Ramsey

To run in dev on Linux:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
Windows Powershell:
first refresh powershell in VS Code using ctrl+shift+`
```
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask run
```

To Deploy
```
pip install wheel
python setup.py bdist_wheel
```
Then copy to server, then
```
mkdir projectfolder
cd projectfolder
python3 -m venv venv
. venv/bin/activate
pip install flaskr-1.0.0-py3-none-any.whl
```
Then setup env
```
export FLASK_APP=flaskr
flask init-db
```
Change Secret Key by generating a random one
```
python -c 'import os; print(os.urandom(16))'
```
and copying it into
```
venv/var/flaskr-instance/config.py
```
```
SECRET_KEY = <output of random>
```
