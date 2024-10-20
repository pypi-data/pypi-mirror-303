from setuptools import setup, find_packages

with open("README.md", 'r') as file:
    description = file.read()

setup(
    name="pygutz",
    version="0.1.1",
    packages=find_packages(),
    author="Nutchapon",
    author_email="nutchapon.met1002@gmail.com",
    maintainer="Nutchapon",
    license="MIT",
    install_requires=[
        "click",
        "fastapi[standard]",
        "uvicorn",
        "SQLAlchemy",
        "pydantic",
        "pydantic-settings"
    ],
    entry_points={
        "console_scripts": [
            "pygutz = pygutz:command_executor"
        ]
    },
    long_description=description,
    long_description_content_type="text/markdown"
)