# ai2project

## For macOs

### Pre-requirements
1. Python 3.6.1
2. virtualenv package. To install: pip install virtualenv

### Install
1. Make sure to create a virtual environment:
python -m virtualenv <name of virtualenv>
ex. python -m virtualenv ai2  # ai2 is the name of the virtual env.

2. Enter virtual environment:
source <name of virtual env>/bin/activate
ex. source ai2/bin/activate

3. Make sure you are in the root directory

4. Install all dependencies:
pip install -r requirements.txt

5. try to run:
python recognizer.py


## For windows

### Pre-requirements
1. at least Python 3.6.1
2. virtualenvwrapper-win package. To install: pip install virtualenvwrapper-win

### Install
1. Make sure to create a virtual environment:
mkvirtualenv <name of virtualenv>
ex. mkvirtualenv ai2  # ai2 is the name of the virtual env.

2. Enter virtual environment:
workon <name of virtual env>
ex. workon ai2

3. Make sure you are in the root directory

4. Install all dependencies:
pip install -r requirements.txt

5. try to run:
python populator.py
