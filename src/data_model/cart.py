from databaser.data_model import DataModel
from databaser.db_parser.table_structure.create_table import TableField
from databaser.db_parser.table_structure.references_fk import ReferencesFK

from config import conn_string
from src.core.database.data_types import DataType
from src.data_model.book import Book
from src.data_model.customer import Customer


class CartItem(DataModel):
    table_name = 'ca_cart_items'

    def __init__(self):

        self.fields = [
            TableField(name='cai_id', data_type=DataType.SERIAL.value, primary_key=True, not_null=False),
            TableField(name='cu_id', data_type=DataType.INTEGER.value, references=ReferencesFK(
                table_name=Customer.table_name,
                field_name="cu_id"
            ).get_sql()),
            TableField(name='b_id', data_type=DataType.INTEGER.value, references=ReferencesFK(
                table_name=Book.table_name,
                field_name="b_id",
            ).get_sql()),
            TableField(name='cai_created_on', data_type=DataType.TIMESTAMPTZ.value, default="CURRENT_TIMESTAMP"),
        ]

        super().__init__(conn_string=conn_string)
