"""
this code section is generate source code template.
"""
def generate_setting_content():
    return  '''from pydantic_settings import BaseSettings, SettingsConfigDict

class Env(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
env = Env()'''

def generate_main_content():
    return '''from core import command_executor

def main():
    command_executor()
    
if __name__=="__main__":
    main()'''

def generate_init_server_content():
    return '''from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes import router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)'''

def generate_init_routes_content():
    return '''from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1"
)

@router.get("/ping")
async def ping():
    return {'message': 'pong'}
'''

def generate_init_pkgs_content():
    return '''from pkgs.logs import Log, LOGGING_CONFIG

logger = Log.getLogger()

"__all__" == ["logger", "LOGGING_CONFIG"]'''

def generate_dbconfig_content():
    return '''"""
this code section about instance database connection.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

# By default we instance postgesql database connection.
DATABASE_URL = "postgresql://user:password@localhost:5432/dbname"

engine = create_engine(DATABASE_URL, echo=True)

session = Session(bind=engine)

class Base(DeclarativeBase):
    """
    Base abtract class instance for map dataclass with database schemas
    """
    pass'''

def generate_log_content():
    return '''import logging
import logging.config as log_conf
from logging import Logger

LOGGING_CONFIG: dict[str,] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s | %(message)s",
            "use_colors": None,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(asctime)s | %(client_addr)s | "%(request_line)s" | %(status_code)s',  # noqa: E501
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "app" : {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s | %(funcName)s/%(filename)s;%(lineno)d | %(message)s",
            "use_colors": None,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "app" : {
            "formatter": "app",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
        "app" : {"handlers": ["app"], "level": "INFO", "propagate": False},
    },
}

class Log:
    def __init__(self) -> None:
        log_conf.dictConfig(LOGGING_CONFIG)
        self.logger = logging.getLogger("app")

    @classmethod
    def getLogger(cls):
        return cls().logger'''

def generate_init_core_content():
    return '''import sys
from core.commands import Command

def command_executor():
    argv = sys.argv
    if len(argv) < 2:
        return
    cmd = Command(argv)
    cmd.execute()'''

def generate_commands_content():
    return '''import os

from pkgs import LOGGING_CONFIG
from core.interfaces.base import BaseCommand


class Command(BaseCommand):
    def __init__(self, argv=None) -> None:
        self.argv = argv
        mode = os.getenv("SERVER_MODE")
        if mode == "" or mode is None:
            self.mode = "debug"
            
        host = os.getenv("SERVER_HOST")
        if host == "" or host is None:
            self.host = "localhost"
            
        port = os.getenv("SERVER_PORT")
        if port == "" or port is None:
            self.port = 8000
    
    def _handle_argv(self):
        try:
            new_argv = self.argv[2:]
            n_argv = len(new_argv)
            
            for index in range(n_argv):
                if new_argv[index] in {"-p","--port"}:
                    self.port = int(new_argv[index + 1])
                elif new_argv[index] in {"-h","--host"}:
                    self.host = new_argv[index + 1]
        except:
            return
        
    def _runapp(self):
        import uvicorn
        
        self._handle_argv()
        if self.mode == 'debug':
            uvicorn.run("server:app", host=self.host, port=self.port, reload=True, log_config=LOGGING_CONFIG)
        else:
            uvicorn.run("server:app", host=self.host, port=self.port, reload=True, log_config=LOGGING_CONFIG)
            
    def execute(self):
        if self.argv is None or len(self.argv) == 0:
            return
        if self.argv[1] == "runapp":
            self._runapp()
        elif self.argv[1] == "migrate":
            return
        else:
            return'''

def generate_models_content():
    return '''from pydantic import BaseModel'''

def generate_schemas_content():
    return '''"""
This section of code is about creating a model for mapping to tables schemas in the database. 
This template uses an ORM framework like sqlalchemy, which is widely used in web development 
using the Python language.
"""
from sqlalchemy import (
    String, 
    Integer, 
    Float, 
    DateTime, 
    Date, 
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped, 
    mapped_column, 
    relationship
)'''

def generate_base_content():
    return '''from abc import  ABC, abstractmethod

class BaseCommand(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError()'''

def generate_repositories_content():
    return '''"""
This code section deals with creating an example of communication or data 
transmission between the database layer and the service layer. 
According to the concept of hexanal software architecture, 
the communication between the business logic part and the database part is clearly separated 
and should not be directly connected. But there should be a middleman
to help communicate between the two sides instead.
"""
from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import List, Dict, Any, Sequence
from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, session: Session) -> None:
        self.session = session
        
    @contextmanager
    def _get_session(self):
        with self.session as db:
            try:
                yield db
            except:
                db.rollback()'''

def generate_services_content():
    return '''"""
This code section is a core bussiness logic. Every logic or handle error should be
in this section. It acts as a middleman to receive and send data between the database 
and requests coming through the API and performs various processing about core logic.
"""
from abc import ABC, abstractmethod'''