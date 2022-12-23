# Inholland SMS service - base api

### Prerequisites
* The [Python](https://www.python.org/) interpreter with version 3.11.x as minimum (make sure you add it to your path)
* A Virtualenv (explained below)

### Recommended
* [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)

### How to run
To setup the project make sure you have all the prerequisites!

1. Clone the project using the Git client.

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

### Environment file
TODO

### Add new packages
Please note, make sure you are inside your venv.
1. Install the package using pip.
2. Export the package(s) to a requirements.txt file:
```
$ pip freeze > requirements.txt
```

### Deactivating the virtualenv
```
$ deactivate
```

### Setting up PyLint
Please note, make sure you are inside your venv.
1. Install PyLint:
```
$ pip install pylint
```

2. Run for a specific file:
```
$ pylint FILENAME.py
```
2. Run for all Python files in the Git repo:
```
$ pylint $(git ls-files '*.py')
```