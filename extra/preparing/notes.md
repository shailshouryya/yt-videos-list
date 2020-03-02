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
