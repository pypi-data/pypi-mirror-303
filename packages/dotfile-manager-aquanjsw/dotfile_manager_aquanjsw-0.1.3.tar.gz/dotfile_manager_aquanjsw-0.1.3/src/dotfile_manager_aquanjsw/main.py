from __future__ import annotations

import logging
import os
import socket

import appdirs
import yaml
from sqlmodel import Session, SQLModel, create_engine, select

from . import helper
from .argparser_ import ArgParser
from .logging_ import init_logger
from .model import Host

DEFAULT_DOTFILES_DIR = os.path.expanduser('~/.dotfiles')
DOTFILES_DIR = os.environ.get('DOTFILES_DIR', DEFAULT_DOTFILES_DIR)
DB_FILE = os.path.join(DOTFILES_DIR, 'sqlite.db')
APP_NAME = 'dotfile-manager'
APP_AUTHOR = 'aquanjsw'
USER_CONFIG_DIR = appdirs.user_config_dir(APP_NAME, APP_AUTHOR)
CONFIG_FILE = os.path.join(USER_CONFIG_DIR, 'config.yaml')

# Populate module level variables
os.environ['APP_NAME'] = APP_NAME
os.environ['APP_AUTHOR'] = APP_AUTHOR
os.environ['USER_CONFIG_DIR'] = USER_CONFIG_DIR
os.environ['DOTFILES_DIR'] = DOTFILES_DIR
os.environ['CONFIG_FILE'] = CONFIG_FILE
os.environ['DB_FILE'] = DB_FILE

logger: logging.Logger | None = None


def main():
    global logger

    parser = ArgParser().get()
    args = parser.parse_args()

    logger = init_logger('DEBUG' if args.verbose else 'INFO')

    # Check database dir
    os.makedirs(DOTFILES_DIR, exist_ok=True)

    engine = create_engine(f"sqlite:///{DB_FILE}")
    SQLModel.metadata.create_all(engine)

    # Check if this host is already registered
    with Session(engine) as session:
        check_registration(session)

    args.func(engine, args)


def check_registration(session: Session):
    assert logger is not None

    if not os.path.exists(CONFIG_FILE):
        check_config_file()

    check_db(session)


def check_config_file():
    config = {}

    host_id = input('Enter host ID (default %s): ' % socket.gethostname())
    host_id = host_id or socket.gethostname()

    config.update({'host_id': host_id})

    os.makedirs(USER_CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        yaml.safe_dump(config, f)


def check_db(session):
    # Check if host_id already exists in the database
    host_id = helper.get_host_id()
    host_id_query = session.exec(select(Host).where(Host.id == host_id)).first()
    if not host_id_query:
        host = Host(id=host_id, platform=helper.get_platform())
        session.add(host)
        session.commit()
