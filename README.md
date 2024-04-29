# API Generate Password
API for generate a strong password.

## SUMMARY
1. [Description](#description)
2. [Valid Characters](#valid-characters)
3. [Dependencies](#dependencies)
4. [Project's Structure](#projects-structure)
5. [Unit Tests](#unit-tests)
6. [How To Run?](#how-to-run)
7. [API Routes](#api-routes)
8. [Model Structure](#model-structure)
9. [How It Works?](#how-it-works)
10. [System Steps](#system-steps)
11. [The End](#the-end)

### Description
*This API has the intent of generate strong passwords to you set into the register of web services. You just need to set
your options, then our system will take your information to generate random passwords.*

*This project uses asynchronous programming concepts and unit tests.*

### Valid Characters
The generated password can contain:

1. Numbers `0 ... 9`;
2. Low Case `a ... z`;
3. Up Case `A ... Z`;
4. Special Characters 1 `!#$%&()*+,-./:;=?@[]{|}`;
5. Special Characters 2 `<>^~¢£§¬`;

### Dependencies
1. [Python3](https://www.python.org/);
2. [Pip](https://pip.pypa.io/en/stable/installation/);
3. [Pytest](https://docs.pytest.org/);
4. [FastAPI](https://fastapi.tiangolo.com/);
5. [Uvicorn](https://www.uvicorn.org/);
6. [Httpx](https://www.python-httpx.org/);
7. [Anyio](https://anyio.readthedocs.io/);
8. [Twisted](https://twisted.org/);
9. [Pytest Asyncio](https://pytest-asyncio.readthedocs.io/);
10. [Pytest Torn Async](https://github.com/eukaryote/pytest-tornasync);
11. [Pytest Trio](https://github.com/python-trio/pytest-trio);
12. [Pytest Twisted](https://github.com/pytest-dev/pytest-twisted);
13. [Python DotEnv](https://github.com/theskumar/python-dotenv);
14. [PyLint](https://pypi.org/project/pylint/);

> **NOTE:** The project dependencies list can be found on the file [requirements.txt](requirements.txt)

To install the `requirements.txt` file, just type or paste it on a Terminal window:

**Have a problem?** Please visit the section of [questions](#possible-questions) here.

```commandline
pip install -r requirements.txt
```

### Project's Structure
Loot at an basic explanation of each *package* in *src*.

```command
src/             -> where source files are in.
|----app/        -> where is the fastapi app.
|----controller/ -> controller and attach to service.
|----exceptions/ -> exceptions generic are here.
|----generate/   -> where in fact the password is generated.
|----model/      -> model to communcate to the back-end.
|----routes/     -> where are the routes of this API.
|----service/    -> services attach to generate from controller.
|----utility/    -> utilities to check and format data.
tests/           -> unit tests are here.
main.py          -> file to run that project
```

### Unit Tests
This project has the unitary tests configured. We used `pytest` as *unit test provider*. Please check if you installed
the **dependencies** [here](#dependencies) before you consider to run these commands here.

First, I present the directory [tests](/tests), inside it you can find the following structure:

```command
tests/
|----controller/
|----|----test_controller_errors_layer.py
|----|----test_controller_success_layer.py
|----generate/
|----|----test_generate_errors_layer.py
|----|----test_generate_success_layer.py
|----mocks/
|----|----passwords.py
|----routes/
|----|----test_routes_errors_layer.py
|----|----test_routes_success_layer.py
|----service/
|----|----generate_password_service.py
|----|----test_service_errors_layer.py
|----|----test_service_success_layer.py
|----conftest.py
```

As you can see, this is the package `tests/`, and for each tests module, we have a class.

To run these tests you have two options:

1. Run by IDE resource;
2. Run by a command on Terminal;

To Run by command line, paste this on Terminal:

```commandline
pytest
```

IDE Case:

> **NOTE:** At this point I won't talk about IDE, please search for the IDE you use and how to run this by it.

### How To Run?
Please review the last Chapter *Dependencies* and install them all. If it ran successfully, you are ready to run.

To make it, just run the file: [`main.py`](/main.py). It is configured.

On the root directory [here]() of that project, just type:

For Windows:

```commandline
py app.py
```

For macOS:

```commandline
python app.py
```

For Linux Distros:

```commandline
python3 app.py
```

**If you find a problem**, review [dependencies](#dependencies) chapter.

### API Routes
Here you can see the routes to that API.

```commandline
Generate a New Password:

method: POST
url: /api/generate/password
body attributes:
  numbers: null
  low_case: null
  up_case: null
  special_char_1: null
  special_char_2: null
  length: 0
```

### Model Structure
Here you can see the class structure to send data to back-end.

* **Password**

| attribute      | type | default |
|:---------------|:-----|:--------|
| numbers        | bool | None    |
| low_case       | bool | None    |
| up_case        | bool | None    |
| special_char_1 | bool | None    |
| special_char_2 | bool | None    |
| length         | int  | 0       |

* **Password JSON Format**

```json
{
  "numbers": true,
  "low_case": true,
  "up_case": true,
  "special_char_1": null,
  "special_char_2": null,
  "length": 32
}
```

> **Remember: except length, the other variables if used, you need to set boolean value (true/false).**

### How It Works?
Description about the steps this software works. It's divided between *User* and *System* requirements.

1. User set information to `model`;
2. System receives the `model` sent by User;
3. So this model is checked, (at least 1 attribute must be `True` value); 
   1. If valid not valid, launch a new exception;
4. count the length and required values range;
5. Use `random.choice` method to get a value and join to the password string;
6. Set the **generated password** to clipboard and returns to the *highest level;*
7. Set the **generated password** to be seen by user;

### System Steps
A resume of [*how it works?*](#how-it-works)

1. User choose parameters;
2. Check parameters;
3. Generate password;
4. Transfer to *clipboard* area;
5. Return the generated password;
6. Let it be seen by user;

### The End
It's a simple project task to make a useful software.

-- *Abel Carvalho*

- [Github Directory's README.md](.github/README.md)

*That's all folks!!!*