import sqlite3


class DbColumn:
    """A class to represent the definition of a database column"""

    # The name of the column
    name: str
    # The type of the column
    field_type: str
    # Whether the column is not null
    not_null: bool
    # The default value of the column
    default_val: str
    # Whether the column is a primary key
    primary_key: bool
    # The raw row data when it's created
    __raw__: sqlite3.Row

    def __init__(self, db_row: tuple[6]):
        """

        :param db_row: The raw row data from the database (e.g., a sqlite3.Row)

        """
        self.name = db_row[1]
        self.field_type = db_row[2]
        self.not_null = db_row[3] == 1 or db_row[5] == 1
        self.default_val = db_row[4]
        self.primary_key = db_row[5] == 1
        self.__raw__ = db_row

    def get_raw(self):
        """Get the original raw row data"""
        return self.__raw__

    def __repr__(self):
        return "Schema({name}, {field_type}, {not_null}, {default_val}, {primary_key})".format(
            name=self.name,
            field_type=self.field_type,
            not_null=self.not_null,
            default_val=self.default_val,
            primary_key=self.primary_key,
        )

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if isinstance(other, DbColumn):
            return (self.__raw__ == other.__raw__) or (
                self.name == other.name
                and self.field_type == other.field_type
                and self.not_null == other.not_null
                and self.default_val == other.default_val
                and self.primary_key == other.primary_key
            )

        return False
