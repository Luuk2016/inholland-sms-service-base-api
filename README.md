# Inholland SMS generator - base api

### Prerequisites
* The <a href="https://www.python.org/">Python</a> interpreter with version 3.7.x as minimum (make sure you add it to your path)
* A Virtualenv (explained below)

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

5. Run the app:
```
$ flask run
```

### When adding new packages
Install the new package using pip.
If pipreqs is already installed, go to step 2.

1. Install pipreqs:
```
$ pip install pipreqs
```
2. Export the packages to a requirements.txt file:
```
$ pipreqs 
```

### Deactivating the venv
```
$ deactivate
```