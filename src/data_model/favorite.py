from databaser.data_model import DataModel
from databaser.db_parser.table_structure.create_table import TableField

from config import conn_string
from src.core.database.data_types import DataType


class Favorite(DataModel):
    table_name = 'fa_favorite'

    def __init__(self):

        self.fields = [
            TableField(name='fa_id', data_type=DataType.SERIAL.value, primary_key=True, not_null=False),
            TableField(name='cu_id', data_type=DataType.INTEGER.value, not_null=False),
            TableField(name='b_id', data_type=DataType.INTEGER.value, not_null=False),
            TableField(name='fa_created_on', data_type=DataType.TIMESTAMPTZ.value, default="CURRENT_TIMESTAMP"),
        ]

        super().__init__(conn_string=conn_string)
