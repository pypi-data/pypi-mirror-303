import os
import sqlite3

from .read import get_schemas
from .gen_common import SUPPORTED_EXT
from .gen_rt import get_rs_code
from .gen_ts import get_ts_code


class CodeGeneratorPathError(Exception):
    """
    The path to the database or destination folder is invalid
    """

    pass


class UnsupportedExtensionError(Exception):
    """
    The code extension (e.g., .ts) is not supported
    """

    pass


CONVERT_MAP = {
    "ts": get_ts_code,
    "rs": get_rs_code,
}


def generate_code(src_db_path: str, dest_folder: str, code_ext: str) -> str:
    if src_db_path is None:
        raise CodeGeneratorPathError("No database path provided")
    if not os.path.exists(src_db_path):
        raise CodeGeneratorPathError("Database path does not exist")
    if not os.path.exists(dest_folder):
        raise CodeGeneratorPathError("Destination folder does not exist")
    if not code_ext or (code_ext.lower() not in SUPPORTED_EXT):
        raise UnsupportedExtensionError("Unsupported code extension")

    schemas = []
    with sqlite3.connect(src_db_path) as conn:
        cursor = conn.cursor()
        schemas = get_schemas(cursor)

    for table, columns in schemas.items():
        code = CONVERT_MAP[code_ext](table, columns)
        dest_file = os.path.join(dest_folder, table + "." + code_ext)
        with open(dest_file, "w") as f:
            f.write(code)
