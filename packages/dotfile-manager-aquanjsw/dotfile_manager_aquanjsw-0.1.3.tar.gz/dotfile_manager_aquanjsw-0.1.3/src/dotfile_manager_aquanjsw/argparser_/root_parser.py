import argparse
import importlib.metadata

from .subparser import QueryParser, RegisterParser, SyncParser


class RootParser:
    def __init__(self):
        # Top-level parser
        parser = argparse.ArgumentParser(
            description='''Manage and sync dotfiles across multiple hosts.

By default, folder '~/.dotfiles' will be used as the database directory, you can
change it by setting the environment variable `DOTFILES_DIR`.
            ''',
            formatter_class=argparse.RawTextHelpFormatter,
        )
        parser.add_argument(
            '-V',
            '--version',
            action='version',
            version=importlib.metadata.version('dotfile_manager_aquanjsw'),
        )
        parser.add_argument(
            '-v', '--verbose', action='store_true', help='Increase output verbosity'
        )
        subparsers = parser.add_subparsers(title='commands', description='')
        RegisterParser(
            parser=subparsers.add_parser(
                'register', help='Register a new entity', aliases=['r']
            ),
        )
        QueryParser(
            parser=subparsers.add_parser(
                'query',
                help='Query all the database',
                aliases=['q'],
                description='Query all the database',
            ),
        )
        SyncParser(
            parser=subparsers.add_parser(
                'sync',
                help='Sync dotfiles across hosts',
                aliases=['s'],
                description='''Sync dotfiles across hosts.

Depending on whether the expression is provided or not, the sync operation 
will be different:

- *sync-self*: If the expression is not provided, the sync will be: "self → db/self".
- *sync-host*: If the expression is provided, the sync will be a *sync-self*
  followed by a "db/host → host".
''',
                formatter_class=argparse.RawTextHelpFormatter,
            ),
        )
        parser.set_defaults(func=lambda *_: parser.print_help())

        self._parser = parser

    def get(self):
        return self._parser
