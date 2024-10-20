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


def generate_code(src_db_path: str, dest_folder: str, code_ext: str):
    """
    Generate code from a SQLite database schema
    :param src_db_path: Path to the SQLite database
    :param dest_folder: Path to the destination folder where the schema code will be created
    :param code_ext: The code extension (e.g., .ts)
    """
    if not (src_db_path is not None and os.path.exists(src_db_path)):
        raise CodeGeneratorPathError("Database path does not exist")

    with sqlite3.connect(src_db_path) as conn:
        generate_by_db(conn.cursor(), dest_folder, code_ext)


def generate_by_db(db_cursor: sqlite3.Cursor, dest_folder: str, code_ext: str):
    """
    Generate code from a SQLite database schema
    :param db_cursor: SQLite database cursor
    :param dest_folder: Path to the destination folder where the schema code will be created
    :param code_ext: The code extension (e.g., .ts)
    """
    if not (dest_folder is not None and os.path.exists(dest_folder)):
        raise CodeGeneratorPathError("Destination folder does not exist")
    if not code_ext or (code_ext.lower() not in SUPPORTED_EXT):
        raise UnsupportedExtensionError("Unsupported code extension")

    schemas = get_schemas(db_cursor)

    for table, columns in schemas.items():
        code = CONVERT_MAP[code_ext](table, columns)
        dest_file = os.path.join(dest_folder, table + "." + code_ext)
        with open(dest_file, "w") as f:
            f.write(code)
