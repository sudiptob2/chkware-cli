import os

from chk.infrastructure import exception
from collections import namedtuple
from pathlib import Path
from typing import Dict
from yaml import safe_load


class ChkFileLoader:
    """Loader for CHK files"""

    @staticmethod
    def to_dict(file_name: str) -> Dict:
        """read yml data"""
        with open(file_name, 'r') as yaml_file:
            try:
                return safe_load(yaml_file)
            except:
                raise SystemExit(exception.err_message('fatal.V0003', {'file_name': file_name}))

    @staticmethod
    def is_file_ok(file_name: str) -> bool:
        """Check if chk file exists, extension is okay"""
        if Path(file_name).is_file() and Path(file_name).suffix == '.chk':
            return True

        raise SystemExit(exception.err_message('fatal.V0002'))

    @staticmethod
    def get_mangled_name(file_name: str) -> str:
        file_name = os.path.abspath(file_name)
        return file_name.lower().strip('/').replace('/', '-').replace('\\', '_').replace(':', '~')


# File context that holds file information
FileContext = namedtuple('FileContext', ['root_file', 'mangled_root_file', 'document'])
