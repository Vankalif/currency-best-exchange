from pathlib import Path


def db_path():
    return Path.cwd().parent / 'db'


def sql_scripts_path():
    return Path.cwd().parent / 'models' / 'sql'

