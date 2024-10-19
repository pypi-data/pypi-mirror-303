from __future__ import annotations

import argparse
import logging
import os
import shutil
import tempfile

from sqlmodel import Session, select

from ... import helper
from ...model import Path

logger = logging.getLogger(__name__)


class SyncParser:
    def __init__(self, parser: argparse.ArgumentParser):
        parser.add_argument(
            'expression',
            nargs='*',
            help='Indicate the dotfiles to be synced: [HOST [APP [DOTFILE]]]',
        )
        parser.add_argument('-f', '--force', action='store_true', help='Skip diffing')
        parser.set_defaults(func=self._resolve)

    def _resolve(self, engine, args: argparse.Namespace):
        with Session(engine) as session:
            if not args.expression:
                sync_self(session)
                return
            sync_host(session, args.expression)


def sync_self(session: Session):
    logger.info(f'Sync: {helper.get_host_id()} → repo/{helper.get_host_id()}')
    path_instances = session.exec(
        select(Path).where(Path.host_id == helper.get_host_id())
    ).all()
    for path_instance in path_instances:
        src_path = path_instance.path
        if helper.get_datetime(src_path) <= path_instance.datetime:
            continue
        dst_path = helper.get_dotfile_path_in_repo(
            helper.get_host_id(),
            path_instance.app_id,
            path_instance.dotfile_name,
        )
        # Update file
        shutil.copyfile(src_path, dst_path)
        logger.info(f'  {src_path} → {dst_path}')
        # Update datetime
        path_instance.datetime = helper.get_datetime(src_path)
        session.add(path_instance)
        session.commit()
        session.refresh(path_instance)


def sync_host(session: Session, expression: list[str]):
    host_id = expression[0]
    if host_id != helper.get_host_id():
        sync_self(session)

    logger.info('Sync: repo/%s → %s', host_id, helper.get_host_id())

    if len(expression) == 1:
        wheres = [Path.host_id == host_id]
    elif len(expression) == 2:
        wheres = [Path.host_id == host_id, Path.app_id == expression[1]]
    elif len(expression) == 3:
        wheres = [
            Path.host_id == host_id,
            Path.app_id == expression[1],
            Path.dotfile_name == expression[2],
        ]
    path_instances_host = session.exec(select(Path).where(*wheres)).all()

    def get_dst_path(app_id, dotfile_name):
        try:
            path_instance = session.exec(
                select(Path).where(
                    Path.host_id == helper.get_host_id(),
                    Path.app_id == app_id,
                    Path.dotfile_name == dotfile_name,
                )
            ).one()
            return path_instance.path
        except Exception as e:
            return ''

    for path_instance in path_instances_host:
        if path_instance.private:
            continue
        dst = get_dst_path(path_instance.app_id, path_instance.dotfile_name)
        if not dst:
            continue
        src = helper.get_dotfile_path_in_repo(
            host_id,
            path_instance.app_id,
            path_instance.dotfile_name,
        )
        os.system(f'git diff {dst} {src}')
        while True:
            key = input(f'Sync: {src} → {dst} ? [y/N] ').lower()
            if key == 'y':
                choose_sync(src, dst)
                break
            elif key in ['', 'n']:
                logger.info('Skipped: %s → %s', src, dst)
                break
            else:
                continue


def choose_sync(src, dst):
    while True:
        key = input('Interactive diff edit? [Y/n] ').lower()
        if key in ['', 'y']:
            choose_interactive_sync(src, dst)
            break
        elif key == 'n':
            shutil.copyfile(src, dst)
            logger.info('Synced: %s → %s', src, dst)
            break
        else:
            continue


def choose_interactive_sync(src, dst):

    # We operate on temp files
    src_tmp = tempfile.mktemp('.src')
    dst_tmp = tempfile.mktemp('.dst')
    shutil.copyfile(src, src_tmp)
    shutil.copyfile(dst, dst_tmp)

    input(f'Note: you should edit {src_tmp}. Press Enter to continue...')
    diff_edit(src_tmp, dst_tmp)

    # Ask again to confirm the sync
    while True:
        key = input('Confirm the sync? [Y/n] ').lower()
        if key in ['', 'y']:
            shutil.copyfile(src_tmp, dst)
            logger.info('Synced: %s → %s', src, dst)
            break
        elif key == 'n':
            logger.warning('Sync canceled.')
            break
        else:
            continue


def diff_edit(file1, file2):
    """
    Use `TERM_PROGRAM` to determine the vscode or not.
    Otherwise use neovim.
    """
    if os.getenv('TERM_PROGRAM') == 'vscode':
        os.system(f'code -w --diff {file1} {file2}')
    else:
        # neovim
        os.system(f'nvim -d {file1} {file2}')
