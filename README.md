# AirBnB_clone

The objective of the project is to recreate a copy of the AirBnB website, with a series of tasks until the website is completed.
The first part consists of developing the console, this goes from the back-end side with the Python programming language.

# What's a command interpreter?
A command interpreter is the part of a computer operating system that understands and executes commands that are entered interactively by a human being or from a program. In some operating systems, the command interpreter is called the shell.

# Using the Console
The clone AirBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

interactive mode:
```
$ AirBnB_clone$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
And in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## FILES

|File Name   |  Description |
| ---    | --- |
|console.py |Hbnb command interpreter|
|models/__init__.py | Contructor for the models Package and create an instance from FilesStorage|
|models/base_model.py |Module that holds a class BaseModel that is the main class in the project|
|models/user.py|Module that holds User class that inherits from BaseModel|
|models/state.py|Module that holds State class that inherits from BaseModel  |
|models/city.py |Module that holds City class that inherits from BaseModel|
|models/amenity.py |Module that holds Amenity class that inherits from BaseModel|
|models/place.py |Module that holds Place class that inherits from BaseModel|
|models/engine/__init__.py|Contructor for the engine Package|
|models/engine/file_storage.py|Module that holds the class FileStorage that handle all serialization-deserialization, to a JSON file for a persistent model|
|tests/|Module with all the unitest for each .py file|
|README.md| description the project|
|    | |

# Authors

[Cristian Rua](https://github.com/Crua0316/AirBnB_clone)
       
[Milena Molina Montoya](https://github.com/MIlenaMontoya/simple_shell)
        

