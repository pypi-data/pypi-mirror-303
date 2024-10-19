It makes it easier to install and manage dependencies for development and testing, separate from the dependencies required for production.
requirements.txt is used to specify the dependencies required to run the production code of a Python project, while requirements_dev.txt is used to specify the dependencies required for development and testing purposes.
We use if for the testing in the python package testing against different version of the python
Run commands
Its a combination of the (virtualenvwrapper and makefile)
It creates a .tox
pyproject.toml
it is being used for configuration the python project it is a alternative of the setup.cfg file. its containts configuration related to the build system such as the build tool used package name version author license and dependencies
In summary, setup.cfg is used by setuptools to configure the packaging and installation of a Python projec
types of testing
Automated testing
Manual testing
Mode of testing
Unit testing
Integration tests
Testing frameworks
pytest
unittest
robotframework
selenium
behave
doctest
check with the code style formatting and syntax(coding standard)
pylint
flake8(it is best because it containt 3 library pylint pycodestyle mccabe)
pycodestyle