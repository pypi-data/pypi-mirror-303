# Pygutz
### This is a generator project APIs web framework toolkit
`pygutz` is a tool that helps manage the creation of 
FastAPI framework projects according to various software architectural design patterns.
By default `pygutz` is set to create web APIs projects as follows a Hexagonal Architechture or plug and adapter patterns.

In the future, we plan to add new design patterns to this package to provide developers with more options for using architectural patterns in software development.
## Installation
```sh
$ pip install pygutz
```
### Run
Run command line to generate project:
```sh
$ pygutz createproject
```
you will get fastapi project struture like is:
```
├── app
│   ├── core
│   │   ├── __init__.py
│   │   ├── commands.py
│   │   ├── entities
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   ├── interfaces
│   │       ├── __init__.py
│   │       ├── base.py
│   │       ├── services.py
│   │       ├── repositories.py
│   ├── pkgs
│   │   ├── __init__.py
│   │   ├── logs.py
│   │   ├── database.py
│   │   ├── utils.py
│   ├── server
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   ├── middlewares.py
│   │   ├── routes
│   │       ├── __init__.py
│   ├── services
│   │   ├── __init__.py
│   ├── repositoies
│   │   ├── __init__.py
│   ├── main.py
│   ├── settings.py
│   ├── __init__.py
├── tests
│   ├── __init__.py
├── .gitignore
```
By defaut project will be set folder `app` name

if you want to define project name can do this:
```sh
$ pygutz createproject --project-name myapp
```
```
├── myapp
│   ├── core
│   │   ├── __init__.py
│   │   ├── commands.py
│   │   ├── entities
```
## Dependencies

Pygutz depends on FastAPI, Uvicorn, SQLAlchemy, Pydantic, click.
- [`fastapi`](https://fastapi.tiangolo.com/) - for the APIs web framework.
- [`uvicorn`](https://www.uvicorn.org/) - for the server that loads and servers your application. 
- [`sqlalchemy`](https://www.sqlalchemy.org/) - for the Python SQL Toolkit and Object Relational Mapper.
- [`pydantic`](https://docs.pydantic.dev/latest/) - for the data serializer.
- [`click`](https://click.palletsprojects.com/en/8.1.x/) - for the cli tools.
- [`pydantic-settings`](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) - for settings management.

## License
This project is licensed under the terms of the MIT lincense.
