[![Python application](https://github.com/ramigiki/passwordfactory/actions/workflows/app.yml/badge.svg?branch=main)](https://github.com/ramigiki/passwordfactory/actions/workflows/app.yml)

## Password factory

A Flask application that generate passwords on demand.

### Directory structure

This repository contains code for **Password Factory**:

* ``app/`` -- contains code for api, schema, utilities and logger
* ``docker/`` -- docker-compose file and docker files for nginx and webapp. It also contains configs for uwsgi and nginx
* ``tests/`` -- Unit test scripts and Data
* ``postman/`` -- postman collection along with api tests
* ``logs/`` -- Application generated logs will store here

### Necessary files in the root directory

* ```.env``` -- contatins the server default params. If any param is missing in the API call, it would be filled from this file.
* ```.flake8``` -- configurations for linting the code
* ```Makefile``` -- contains the automation scripts
* ```pytest.ini``` -- configurations for testing and coverage report
* ```requirements.txt``` -- lists all the dependencies of the application
* ```tests_requirements.txt``` -- list all the dependencies for running the tests.

---

### Running Development Environment

>**Note**: _Make sure you have [python3](https://www.python.org/downloads/)_ installed

* Clone the repository
* Navidate into the code directory

    ```bash
    cd <directory>
    ```

* Run the following command to create virtual environment

    ```bash
    python3 -m venv venv
    ```

* Activate the virtual enviroment using the following command

    ```bash
    source venv/bin/activate
    ```

* Now start dev server using the following command. It will install dependencies and run the developement server on localhost default port 5000 : <http://localhost:5000/generate?numbers=1>

    ```bash
    make start-dev
    ```

* Import the postman collection from the ``postman/`` directory and set environment to 'Password factory' and baseurl to {{local}}.

* Run the API calls to test

---

### Running Docker Instance (Calibrated for production)

>**Note**: _Make sure you have installed [docker](https://docs.docker.com/install/) and
[docker-compose](https://docs.docker.com/compose/install/)._

* Clone the repository

* Navidate into the code directory

    ```bash
    cd <directory>
    ```

* To fireup docker containers using docker-compose:

    ```bash
    make start-docker
    ```

* The application would be served at <http://localhost/generate?numbers=1>

* To stop docker containers:

    ```bash
    make stop-docker
    ```

* To build docker images from the docker files:

   ```bash
    make build-docker
    ```

* Import the postman collection in the ``postman/`` directory and set environment to 'Password factory' and baseurl to {{docker}}.

* Run the API call to test

---

### Creating distribution for packaging

* Clone the repository

* Navidate into the code directory

    ```bash
    cd <directory>
    ```

* To create distribution files run command

    ```bash
    make dist

    ```

>**Note** A dist directory will be created with tar.gz file. It can be published and installed using setup.py commands

---

### Continuous Integration Pipeline

>**Note**: Github Actions are used for continuous integration

* Checks performed on commit to main

    ```text
    - Run linter to check code standards
    - Run pytest to execute tests

    ```

* Code will be merged to main branch once the checks are successfull

---

### Other Helpful Commands

To only install requirements:

```bash
make install
```

To run unit tests:

```bash
make test
```

To run code linting:

```bash
make lint
```

To format code:

```bash
make format
```

---

### API documentation and testing

* ``postman/`` -- contains api collection and test cases.

* Each API has a documentation section to explain the scenario.

* 40 postman API tests are in the collection to test API.

* Import the collection and execute run collection.

---

### Flowchart diagram of /generate api call

>**Note** Diagram is created using mermaid code, only visible in repository.

```mermaid
graph TD
    A[Request password: '/generate'] -->|Gets params and calls| B(Password Factory)
    B --> C{Validate params}
    C -->|Incorrect params| E[Return 404 Bad Request]
    E -->id1([Done])
    C -->|Correct params| F[Generate Password]
    F -->G[Return password to user]
    G -->Hid1([Done])
```

---

### Best practices followed during the development

* Followed the rule of simplicity. Simple is better than complex.

* Code distribution across modules and files to ensure separation of concern.

* Custom logging with user readable message format and log rotation.

* Handled error such that they get noticed. log file is maintained incase error in the console is missed.

* In docker implementation, reverse proxy through nginx to ensure api calls donot fall on flask app directly (best practice to ensure security).

* Continuous integration implemented to make sure code is not buggy and upto the set standard.

* .env file varibales are overridden by env variables exported through export command.

* virtual environment used to make sure dependencies are installed in the env.  

* Marshmallow schema for validation of API request.

* flake8 is used for linting code.

* black is used for formating code.

* setup.py implemented for distribution packages.

* test cases implementation.
