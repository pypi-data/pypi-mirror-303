# gitco

---
Let's install some required tools

```bash
>>> pip install -U pip setuptools
```

---
## Step 1: Create an importable module!

Let's create some python script called "gitco.py"

```python
def gen_commit_msg():
	print("My commit msg")
```

Let's confirm that it can be imported properly:

```bash
>>> python -c "import gitco; gitco.gen_commit_msg()"
```

---
## Step 2: Create setup.py

setup.py is used to tell pip how to install the package. You can find the full documentation (here)[https://setuptools.readthedocs.io/en/latest/setuptools.html].

```python
from setuptools import setup, find_packages
from gitco import __version__

setup(
    name='gitco',
    version=__version__,

    install_requires=[
        'instructor',
        'openai',
        'requests',
        'python-dotenv',
    ],

    url='https://github.com/Valkea/gitco',
    author='Emmanuel Letremble (Valkea)',
    author_email='gitco@shedge.com',

    packages=find_packages()
)
```

Add this to gitco.py:

```python
__version__ = 'dev'
```

To confirm that setup.py works properly:

```bash
>>> pip install -e .
```

It should install the package and create a folder called gitco.egg-info.


Run the following script to check it's still working
```bash
>>>python -c "from gitco import gen_commit_msg; gen_commit_msg()"
```
