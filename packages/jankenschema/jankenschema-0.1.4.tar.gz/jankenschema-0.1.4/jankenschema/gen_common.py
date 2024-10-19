TYPE_MAP = {
    "TEXT": {
        "ts": "string",
        "rs": "String",
    },
    "INT": {
        "ts": "number",
        "rs": "isize",
    },
    "INTEGER": {
        "ts": "number",
        "rs": "isize",
    },
    "REAL": {
        "ts": "number",
        "rs": "f64",
    },
}

SUPPORTED_EXT = TYPE_MAP["TEXT"].keys()
