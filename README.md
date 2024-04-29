# API Generate Password
API for generate a strong password.

## SUMMARY
1. [Description](#description)
2. [Valid Characters](#valid-characters)
3. [Dependencies](#dependencies)
4. [How To Run?](#how-to-run)
5. [API Routes](#api-routes)
6. [Model Structure](#model-structure)
7. [How It Works?](#how-it-works)
8. [System Steps](#system-steps)
9. [Possible Questions](#possible-questions)
10. [The End](#the-end)

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
1. Python3;
2. Pip;
3. Pytest
4. FastAPI;
5. Uvicorn;
6. Httpx;
7. Anyio;
8. Twisted;
9. Pytest Asyncio;
10. Pytest Torn Async;
11. Pytest Trio;
12. Pytest Twisted;

> **NOTE:** The project dependencies list can be found on the file [requirements.txt](requirements.txt)

To install the `requirements.txt` file, just type or paste it on a Terminal window:

**Have a problem?** Please visit the section of [questions](#possible-questions) here.

```commandline
pip install -r requirements.txt
```

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

### Possible Questions

<details>
    <summary>
        Question?
    </summary>
    <p>
        Answer.
    </p>
</details>

### The End
It's a simple project task to make a useful software.

-- *Abel Carvalho*

*That's all folks!!!*