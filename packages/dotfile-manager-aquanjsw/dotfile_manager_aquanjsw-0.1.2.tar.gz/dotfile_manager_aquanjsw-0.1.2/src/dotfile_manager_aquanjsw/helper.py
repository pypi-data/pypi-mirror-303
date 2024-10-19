import datetime
import os
import sys

import yaml


def get_platform():
    return sys.platform


def get_datetime(file):
    return datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime(
        '%Y-%m-%d %H:%M:%S'
    )


def save_host_id(host_id):
    config_in = {'host_id': host_id}
    os.makedirs(os.environ['USER_CONFIG_DIR'], exist_ok=True)
    with open(os.environ['CONFIG_FILE']) as f:
        config = yaml.safe_load(f)
        config.update(config_in)
    with open(os.environ['CONFIG_FILE'], 'w') as f:
        yaml.safe_dump(config, f)


def get_host_id():
    with open(os.environ['CONFIG_FILE']) as f:
        config = yaml.safe_load(f)
    return config['host_id']


def get_dotfile_path_in_repo(*components):
    """
    :param components: [HOST_ID, [APP_ID, [DOTFILE_NAME]]]
    """
    return os.path.join(os.environ['DOTFILES_DIR'], *components)
