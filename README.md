# Voice-Based-Email

Python Flask Installation
-------------------------

1. Commands for installation
o Creating python virtual environment
- python -m venv {folder_name}
- eg: python -m venv venv

o Activating virtual environment
- ./{folder_name}/Scripts/activate.ps1
- eg: ./venv/Scripts/activate.ps1

o Installing python flask using pip
- First activate virutal environment
- use command: pip install flask

o Select Python Interpreter
- Pres Ctrl + Shift + P
- Select Python: Select Interpreter
- Choose Find Interpreter
- Select venv folder & browse to Scripts -> Python
- Virtual environment will be activated

2. Error Handling in Server
o ERROR: Invalid options object. Dev Server has been initialized using an options object that does not match the API schema. - options.allowedHosts[0] should be a non-empty string.
o SOLUTION: Connect to internet
