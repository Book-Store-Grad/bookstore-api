from databaser.data_model import DataModel
from databaser.db_parser.table_structure.create_table import TableField
from databaser.db_parser.table_structure.references_fk import ReferencesFK

from config import conn_string
from src.core.database.data_types import DataType
from src.data_model.customer import Customer


class Order(DataModel):
    table_name = 'o_order'

    def __init__(self):
        self.schema_name = "public"
        self.server_name = "pgsql"

        self.fields = [
            TableField(name='o_id', data_type=DataType.SERIAL.value, primary_key=True, not_null=True),
            TableField(name='cu_id', data_type=DataType.INTEGER.value, references=ReferencesFK(
                table_name=Customer.table_name,
                field_name="cu_id"
            ).get_sql()),
            TableField(name='o_total', data_type=DataType.INTEGER.value, not_null=True),
            TableField(name='o_created_on', data_type=DataType.TIMESTAMPTZ.value, default="CURRENT_TIMESTAMP"),
        ]

        super().__init__(conn_string=conn_string)
