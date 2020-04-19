- [Python packaging: get Development Status from version string](https://stackoverflow.com/questions/24475318/python-packaging-get-development-status-from-version-string) - Stack Overflow
- [Build Your First pip Package](https://dzone.com/articles/executable-package-pip-install) - DZone: Big Data Zone, by Deepak Kumar; Sep. 19, 2018
  - build: build package information.
  - dist: Contains your .whl file. A WHL file is a package saved in the Wheel format, which is the standard built-package format used for Python distributions. You can directly install a .whl file using pip install some\_package.whl on your system
  - project.egg.info: An egg package contains compiled bytecode, package information, dependency links, and captures the info used by the setup.py test command when running tests.*
- [Python: Creating a pip installable package](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/) - Python for HPC: Community Materials, Stephen Hudson (Software Developer at Argonne)
- [Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.io/) - PyPA » Python Packaging User Guide »
- [An Overview of Packaging for Python](https://python-packaging-user-guide.readthedocs.io/overview/) - PyPA » Python Packaging User Guide »
- [setup.py](https://github.com/pypa/sampleproject/blob/master/setup.py) - [pypa/sampleproject](https://github.com/pypa/sampleproject) GitHub Repo
- *[Classifiers](https://pypi.org/classifiers/)*
- [raw classifiers in text](https://test.pypi.org/pypi?%3Aaction=list_classifiers)
- [install_requires vs requirements files](https://packaging.python.org/discussions/install-requires-vs-requirements/) - PyPA » Python Packaging User Guide » Discussions »
- [pip 19.3.dev0 documentation User Guide](https://pip.pypa.io/en/latest/user_guide/#requirements-files) - PyPA » pip 19.3.dev0 documentation »
- [PEP 440 -- Version Identification and Dependency Specification](https://www.python.org/dev/peps/pep-0440/) - Python>>> Python Developer's Guide>>> PEP Index>>> PEP 440 -- Version Identification and Dependency Specification
- [Python setuptools.find_packages() Examples](https://www.programcreek.com/python/example/10688/setuptools.find_packages) - programcreek
- [Building and Distributing Packages with Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html) - setuptools 41.2.0 documentation »
- [What is “where” argument for in setuptools.find_packages?](https://stackoverflow.com/questions/51286928/what-is-where-argument-for-in-setuptools-find-packages) - Stack Overflow
- [find_packages](http://code.nabla.net/doc/setuptools/api/setuptools/setuptools.find_packages.html) - setuptools
- [Licenses & Standards](https://opensource.org/licenses) - Open Source Initiative
  - Open source licenses are licenses that comply with the [Open Source Definition](https://opensource.org/osd) — in brief, they allow software to be freely used, modified, and shared. To be approved by the Open Source Initiative (also known as the OSI), a license must go through the [Open Source Initiative's license review process](https://opensource.org/approval).
- [ImportError: “unknown location”](https://forum.learncodethehardway.com/t/importerror-unknown-location/2034) - learncodethehardway
- [Traps for the Unwary in Python’s Import System](https://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html) - Docs » Python Concepts » Traps for the Unwary in Python’s Import System
  - READ THIS!
- [How to create a Python Package with __init__.py](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html) - Timothy Bramlett
- after reading the previous 2, read these
  - [ValueError: attempted relative import beyond top-level package](https://stackoverflow.com/questions/35166821/valueerror-attempted-relative-import-beyond-top-level-package) - Stack Overflow
  - [Relative imports for the billionth time](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912) - Stack Overflow
- [What is __init__.py for?](https://stackoverflow.com/questions/448271/what-is-init-py-for) - Stack Overflow
    - Files named __init__.py are used to mark directories on disk as Python package directories. If you have the files

    ```
    mydir/spam/__init__.py
    mydir/spam/module.py
    ```
    - and mydir is on your path, you can import the code in module.py as

    ``` import spam.module ```
    - or

    ```
    from spam import module
    ```
    - If you remove the __init__.py file, Python will no longer look for submodules inside that directory, so attempts to import the module will fail.

    - The __init__.py file is usually empty, but can be used to export selected portions of the package under more convenient name, hold convenience functions, etc. Given the example above, the contents of the init module can be accessed as

    ```
    import spam
    ```
    - based on [What is __init__.py used for?](https://effbot.org/pyfaq/what-is-init-py-used-for.htm) - effbot

```
Files named __init__.py are used to mark directories on disk as a Python package directories. If you have the files

mydir/spam/__init__.py
mydir/spam/module.py
and mydir is on your path, you can import the code in module.py as:

import spam.module
or

from spam import module
If you remove the __init__.py file, Python will no longer look for submodules inside that directory, so attempts to import the module will fail.

The __init__.py file is usually empty, but can be used to export selected portions of the package under more convenient names, hold convenience functions, etc. Given the example above, the contents of the __init__ module can be accessed as

import spam
```
- [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/) - PyPA » Python Packaging User Guide » Guides »

### closure scoping
- [Don't understand why UnboundLocalError occurs (closure) [duplicate]](https://stackoverflow.com/questions/9264763/dont-understand-why-unboundlocalerror-occurs-closure) - Stack Overflow
- [How do JavaScript closures work?](https://stackoverflow.com/questions/111102/how-do-javascript-closures-work) - Stack Overflow
- [Local (?) variable referenced before assignment [duplicate]](https://stackoverflow.com/questions/11904981/local-variable-referenced-before-assignment) - Stack Overflow
  - [Python 3: UnboundLocalError: local variable referenced before assignment [duplicate]](https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment) - Stack Overflow
  - [Assigning to variable from parent function: “Local variable referenced before assignment” [duplicate]](https://stackoverflow.com/questions/8934772/assigning-to-variable-from-parent-function-local-variable-referenced-before-as?noredirect=1&lq=1) - Stack Overflow
- [UnboundLocalError on local variable when reassigned after first use](https://stackoverflow.com/questions/370357/unboundlocalerror-on-local-variable-when-reassigned-after-first-use) - Stack Overflow
- [Don't understand why UnboundLocalError occurs (closure) [duplicate]](https://stackoverflow.com/questions/9264763/dont-understand-why-unboundlocalerror-occurs-closure) - Stack Overflow
  - Python doesn't have variable declarations, so it has to figure out the [scope](http://docs.python.org/3.3/tutorial/classes.html#python-scopes-and-namespaces) of variables itself. It does so by a simple rule: If there is an assignment to a variable inside a function, that variable is considered local.[1](http://docs.python.org/3.3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python) Thus, the line
  - `counter += 1`
  - implicitly makes `counter` local to `increment()`. Trying to execute this line, though, will try to read the value of the local variable `counter` before it is assigned, resulting in an `[UnboundLocalError](http://docs.python.org/3.3/library/exceptions.html#UnboundLocalError)`.[2](http://docs.python.org/3.3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value)
  - If `counter` is a global variable, the [global](http://docs.python.org/3.3/reference/simple_stmts.html#the-global-statement) keyword will help. If `increment()` is a local function and `counter` a local variable, you can use [nonlocal](http://docs.python.org/3.3/reference/simple_stmts.html#the-nonlocal-statement) in Python 3.x.
  - Sven Marnach answered Feb 13 '12 at 17:15
    - --> python 3 docs has a [faq page on why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value](https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value) via [unboundlocalerror-local-variable-l-referenced-before-assignment-python – here](http://stackoverflow.com/questions/21456739/unboundlocalerror-local-variable-l-referenced-before-assignment-python) May 4 '14 at 7:19
    - --> A note that caught me out, I had a variable declared at the top of the file that I can read inside a function without issue, however to write to a variable that I have declared at the top of the file, I had to use global. – mouckatron Feb 6 '18 at 14:35
    - --> A more in-depth explanation: [docs.python.org/3.3/reference/…](https://docs.python.org/3.3/reference/executionmodel.html#naming-and-binding). Not only can assignments bind names, so can imports, so you may also get UnboundLocalError from a statement that uses an unbounded imported name. Example: `def foo(): bar = deepcopy({'a':1}); from copy import deepcopy; return bar`, then `from copy import deepcopy; foo()`. The call succeeds if the local import `from copy import deepcopy` is removed. – Yibo Yang Jun 27 '18 at 16:00
<br>

  - You need to use the [global statement](http://docs.python.org/py3k/reference/simple_stmts.html#the-global-statement) so that you are modifying the global variable counter, instead of a local variable:
```shell
counter = 0

def increment():
  global counter
  counter += 1

increment()
```
  - If the enclosing scope that `counter` is defined in is not the global scope, on Python 3.x you could use the [nonlocal statement](http://docs.python.org/py3k/reference/simple_stmts.html#the-nonlocal-statement). In the same situation on Python 2.x you would have no way to reassign to the nonlocal name `counter`, so you would need to make `counter` mutable and modify it:
```shell
counter = [0]

def increment():
  counter[0] += 1

increment()
print counter[0]  # prints '1'
```
  - Andrew Clark answered Feb 13 '12 at 17:13
<br>

  - To answer the question in your subject line,* yes, there are closures in Python, except they only apply inside a function, and also (in Python 2.x) they are read-only; you can't re-bind the name to a different object (though if the object is mutable, you can modify its contents). In Python 3.x, you can use the [nonlocal](https://docs.python.org/3/reference/simple_stmts.html?highlight=nonlocal#nonlocal) keyword to modify a closure variable.
```shell
def incrementer():
    counter = 0
    def increment():
        nonlocal counter
        counter += 1
        return counter
    return increment

increment = incrementer()

increment()   # 1
increment()   # 2
```
  - * The question origially asked about closures in Python.
  - kindall answered Feb 13 '12 at 17:21
<br>

  - The reason of why your code throws an `UnboundLocalError` is already well explained in other answers.
  - But it seems to me that you're trying to build something that works like [itertools.count()](http://docs.python.org/library/itertools.html#itertools.count).
  - So why don't you try it out, and see if it suits your case:

>>> from itertools import count
>>> counter = count(0)
>>> counter
count(0)
>>> next(counter)
0
>>> counter
count(1)
>>> next(counter)
1
>>> counter
count(2)
  - Rik Poggi answered Feb 13 '12 at 17:31
<br>

  - Python has lexical scoping by default, which means that although an enclosed scope can access values in its enclosing scope, it cannot modify them (unless they're declared [global](http://docs.python.org/3.3/reference/simple_stmts.html#the-global-statement) with the global keyword).
  - A closure binds values in the enclosing environment to names in the local environment. The local environment can then use the bound value, and even reassign that name to something else, but it can't modify the binding in the enclosing environment.
  - In your case you are trying to treat `counter` as a local variable rather than a bound value. Note that this code, which binds the value of x assigned in the enclosing environment, works fine:
```shell
>>> x = 1

>>> def f():
>>>  return x

>>> f()
1
```
  - Chris Taylor answered Feb 13 '12 at 17:21
<br>

  - To modify a global variable inside a function, you must use the global keyword.
  - When you try to do this without the line
  - `global counter`
  - inside of the definition of increment, a local variable named counter is created so as to keep you from mucking up the counter variable that the whole program may depend on.
  - Note that you only need to use global when you are modifying the variable; you could read counter from within increment without the need for the global statement.
  - chucksmash answered Feb 13 '12 at 17:13
- [How to Do a Binary Search in Python](https://realpython.com/binary-search-python/) - [Real Python](https://realpython.com/), [Bartosz Zaczyński](https://realpython.com/binary-search-python/#author), Mar 16, 2020
- [Python Scope & the LEGB Rule: Resolving Names in Your Code](https://realpython.com/python-scope-legb-rule/) - [Real Python](https://realpython.com/), Leodanis Pozo Ramos;  Mar 18, 2020
  - [Discovering Unusual Python Scopes](https://realpython.com/python-scope-legb-rule/#discovering-unusual-python-scopes)
  - [Using Scope Related Built-In Functions](https://realpython.com/python-scope-legb-rule/#using-scope-related-built-in-functions)
    - `globals()`
    - `locals()`
    - `dir()`
    - `vars()`
