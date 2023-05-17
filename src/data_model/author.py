from databaser.data_model import DataModel
from databaser.db_parser.table_structure.create_table import TableField

from config import conn_string
from src.core.database.data_types import DataType


class Author(DataModel):
    table_name = 'a_author'

    def __init__(self):
        self.fields = [
            TableField(name='a_id', data_type=DataType.SERIAL.value, primary_key=True, not_null=False),
            TableField(name='a_name', data_type=DataType.CHARACTER_VARYING.value),
            TableField(name='a_created_on', data_type=DataType.TIMESTAMPTZ.value, default="CURRENT_TIMESTAMP"),
        ]

        super().__init__(conn_string=conn_string)
