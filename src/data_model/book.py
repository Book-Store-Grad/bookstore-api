from databaser.data_model import DataModel
from databaser.db_parser.table_structure.create_table import TableField

from config import conn_string
from src.core.database.data_types import DataType


class Book(DataModel):
    table_name = 'b_book'

    def __init__(self):
        self.fields = [
            TableField(name='b_id', data_type=DataType.SERIAL.value, primary_key=True, not_null=False),
            TableField(name='b_name', data_type=DataType.CHARACTER_VARYING.value),
            TableField(name='b_description', data_type=DataType.CHARACTER_VARYING.value),
            TableField(name='b_genre', data_type=DataType.CHARACTER_VARYING.value),
            TableField(name='b_price', data_type=DataType.CHARACTER_VARYING.value),
            TableField(name='b_created_on', data_type=DataType.TIMESTAMPTZ.value, default="CURRENT_TIMESTAMP"),
        ]

        super().__init__(conn_string=conn_string)
