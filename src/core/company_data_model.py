from databaser.data_model import DataModel
from databaser.db_parser.table_structure.create_table import TableField

from config import conn_string
from src.core.database.data_types import DataType


class CompanyDataModel(DataModel):
    schema_name = None

    def __init__(self, company_name: str):
        connection_string = conn_string.copy()
        connection_string['database'] = company_name

        super().__init__(conn_string=connection_string)
        # self.schema_name = company_name

        self.fields.append(
            TableField(name='is_active', data_type=DataType.BOOLEAN.value, primary_key=False, default="TRUE",
                       not_null=True,),
        )
