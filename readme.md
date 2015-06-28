# Overview of intent
exercising some good design practices in python in the context of working through a numerical methods textbook

# Set up

##Python
try running a python instance in the terminal, "python", hopefully stuff will happen, if not, install python. 

see what version of pip you have installed, "pip -V" should result in 7.x range of things. if not, either update or install fresh.

https://pip.pypa.io/en/latest/installing.html

##Virtual environment

We're using virtualenv to handle managing dependencies and environment complications.

http://docs.python-guide.org/en/latest/dev/virtualenvs/

### good bits

"pip install virtualenv"

"source venv/bin/activate" in the root directory to start running python from the local environment. May or may not visibly change your terminal, need some guidance on that. To verify that you are in the environment you could try importing a module in the venv that's not in your normal python install, for example

"python" -> terminal instance of python boots up

"import sympy" -> if it works, you're probably in the virtual environment, if it gives an error message, probably not. Results will vary if you have already installed that module in the global scope.

"deactivate" resets your terminal to the global scope.

## ipython notebook
can be a good framework for live coding compared with the terminal.

http://ipython.org/ipython-doc/stable/notebook/index.html

pip install "ipython[notebook]" // should be unncessary if venv is working as expected.

and

ipython notebook

will install