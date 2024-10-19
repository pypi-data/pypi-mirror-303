import argparse
import logging
import os
import shutil

from sqlmodel import Session

from ... import helper
from ...model import Path

logger = logging.getLogger(__name__)


class RegisterParser:
    def __init__(self, parser: argparse.ArgumentParser):
        parser.add_argument('app', help='The app ID')
        parser.add_argument('path', help='The actual path')
        parser.add_argument(
            '-d',
            '--dotfile',
            help='''A short dotfile name for the path. By default, the basename
            of the path will be used as the dotfile name.''',
        )
        parser.add_argument(
            '-p',
            '--private',
            action='store_true',
            help='Make the path private, which will be ignored in sync',
        )
        parser.set_defaults(func=self._resolve)

    def _resolve(self, engine, args: argparse.Namespace):
        """

        Try to insert in to db first and then try to copy the file.
        This may avoid duplicated insertions.
        """

        # Check if the path exists
        if not os.path.exists(args.path):
            logger.warning(
                '%s does not exist, continue by creating an empty one', args.path
            )
            os.makedirs(os.path.dirname(args.path), exist_ok=True)
            open(args.path, 'x').close()

        if not args.dotfile:
            args.dotfile = os.path.basename(args.path)

        path = Path(
            host_id=helper.get_host_id(),
            app_id=args.app,
            dotfile_name=args.dotfile,
            path=args.path,
            private=args.private,
            datetime=helper.get_datetime(args.path),
        )
        with Session(engine) as session:
            session.add(path)
            session.commit()

        # Copy the dotfile to database
        src = args.path
        dst = helper.get_dotfile_path_in_repo(
            helper.get_host_id(), args.app, args.dotfile
        )
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)
