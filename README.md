# Inholland SMS service - base api
[![Pylint](https://github.com/Luuk2016/inholland-sms-service-base-api/actions/workflows/pylint.yml/badge.svg?branch=master)](https://github.com/Luuk2016/inholland-sms-service-base-api/actions/workflows/pylint.yml)
[![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/lkenselaar/inholland-sms-service-base-app)](https://hub.docker.com/repository/docker/lkenselaar/inholland-sms-service-base-app)

### Requirements
#### Minimum
* The [Python](https://www.python.org/) interpreter with version 3.11.x as minimum (make sure you add it to your path)
* A Virtualenv (explained below)
* A PostgreSQL database

#### Recommended
* [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)

### How to run
1. Clone the project using a Git client.

2. Open a terminal and move your working directory to the project.

3. Create a new Virtualenv:
```
$ python3 -m venv venv
```

4. Activate the Virtualenv (macOS/Linux):
```
$ . venv/bin/activate
```
4. Activate the Virtualenv (Windows):
```
venv\Scripts\activate
```

5. Install the requirements:
```
$ pip install -r requirements.txt
```

6. Run the app:
```
$ flask run
```

#### Required environment variables
To run the app, add the following to your environment variables:
```
"DB_CONNECTION_STRING" => "postgresql://USER:PASSWORD@HOST:PORT/DBNAME"
"SECRET_KEY" => "secret"
```
##### Optional
```
"FLASK_SERVER_PORT" => "5000"
```

#### Add new packages
Please note, make sure you are inside your venv.
1. Install the package using pip.
2. Export the package(s) to a requirements.txt file:
```
$ pip freeze > requirements.txt
```

#### Deactivating the virtualenv
```
$ deactivate
```

#### Running PyLint
PyLint should automatically be installed when downloading all dependencies. <br>
Please note, make sure you are inside your venv.
1. Run for a specific file:
```
$ pylint FILENAME.py
```
2. Run for all Python files in the Git repo:
```
$ pylint $(git ls-files '*.py')
```

### Authors
* **[Luuk Kenselaar](https://github.com/Luuk2016)**
* **[Casper van Genderingen](https://github.com/vangenderingen)**
* **[Jeroen Bol](https://github.com/jerohero)**
