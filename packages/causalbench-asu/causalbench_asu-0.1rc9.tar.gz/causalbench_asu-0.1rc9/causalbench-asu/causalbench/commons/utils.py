import atexit
import logging
import os
import shutil
import tempfile
from pathlib import Path
from zipfile import ZipFile

import yaml
from bunch_py3 import bunchify, Bunch


def parse_arguments(args, keywords):
    # parse the arguments
    if len(args) == 0:
        return bunchify(keywords)
    elif len(args) == 1:
        if isinstance(args[0], Bunch):
            return args[0]
        elif isinstance(args[0], dict):
            return bunchify(args[0])
    else:
        logging.error('Invalid arguments')
        return


def causal_bench_path(*path_list) -> str:
    path: Path = Path.home().joinpath('.causalbench')
    for path_str in path_list:
        path = path.joinpath(str(path_str))
    return str(path)


def cached_module(module_id, version, module_type: str) -> str:
    # form the directory path
    dir_path = causal_bench_path(module_type, module_id, version)

    # check if directory exists
    if os.path.isdir(dir_path):
        return dir_path


def extract_module(module_id, version, module_type: str, zip_file: str) -> str:
    # form the directory path
    dir_path = causal_bench_path(module_type, module_id, version)

    # extract the zip file
    with ZipFile(zip_file, 'r') as zipped:
        zipped.extractall(path=dir_path)

    return dir_path


def extract_module_temporary(zip_file: str) -> str:
    # form the directory path
    dir_path = tempfile.TemporaryDirectory().name
    atexit.register(lambda: shutil.rmtree(dir_path))

    # extract the zip file
    with ZipFile(zip_file, 'r') as zipped:
        zipped.extractall(path=dir_path)

    return dir_path


def package_module(state, package_path: str, entry_point: str = 'config.yaml') -> str:
    zip_file = tempfile.NamedTemporaryFile(delete=True, suffix='.zip').name
    atexit.register(lambda: os.remove(zip_file))

    with ZipFile(zip_file, 'w') as zipped:
        if entry_point:
            zipped.writestr(entry_point, yaml.safe_dump(state, sort_keys=False, indent=4))

        if package_path is not None:
            for root, dirs, files in os.walk(package_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipped_file_path = os.path.relpath(os.path.join(root, file), package_path)
                    if zipped_file_path != entry_point:
                        zipped.write(file_path, zipped_file_path)

    return zip_file
