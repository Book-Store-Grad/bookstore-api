from databaser.data_model import DataModel
from databaser.db_parser.table_structure.create_table import TableField

from config import conn_string
from src.core.database.data_types import DataType


class Customer(DataModel):
    table_name = 'cu_customer'

    def __init__(self):
        self.schema_name = "public"
        self.server_name = "pgsql"

        self.fields = [
            TableField(name='cu_id', data_type=DataType.SERIAL.value, primary_key=True, not_null=False),
            TableField(name='cu_name', data_type=DataType.CHARACTER_VARYING.value),
            TableField(name='cu_email', data_type=DataType.CHARACTER_VARYING.value),
            TableField(name='cu_password', data_type=DataType.CHARACTER_VARYING.value),
            TableField(name='cu_image_url', data_type=DataType.CHARACTER_VARYING.value),
            TableField(name='cu_role', data_type=DataType.CHARACTER_VARYING.value, default="'CUSTOMER'"),
            TableField(name='cu_created_on', data_type=DataType.TIMESTAMPTZ.value, default="CURRENT_TIMESTAMP"),
        ]

        super().__init__(conn_string=conn_string)
