import argparse
import logging
import os

import tabulate
from sqlmodel import Session, select

from ...model import Path

logger = logging.getLogger(__name__)


class QueryParser:
    def __init__(self, parser: argparse.ArgumentParser):
        parser.add_argument(
            'expressions',
            nargs='*',
            help='''The query expressions for path table,
            e.g. 'host_id == "A"' 'app_id == "bash"'
            ''',
        )
        parser.set_defaults(func=self._resolver)

    @staticmethod
    def _get_clauses(expressions):
        clauses = []
        for expression in expressions:
            expression = 'Path.' + expression.strip()
            locals = {}
            exec(f'clause = {expression}', globals(), locals)
            clauses.append(locals['clause'])
        return clauses

    @staticmethod
    def _resolver(engine, args):
        with Session(engine) as session:
            paths = session.exec(
                select(Path).where(*QueryParser._get_clauses(args.expressions))
            ).all()
        print(
            tabulate.tabulate(
                [
                    (
                        path.host_id,
                        path.app_id,
                        path.dotfile_name,
                        path.path,
                        path.private,
                        path.datetime,
                    )
                    for path in paths
                ],
                headers=[
                    'host_id',
                    'app_id',
                    'dotfile_name',
                    'path',
                    'private',
                    'datetime',
                ],
                tablefmt='grid',
            )
        )
        logger.info(f'From {os.environ["DB_FILE"]}')
