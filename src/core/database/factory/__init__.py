"""
    This module will act as a factory for the database entities
    Simply, it will create all tables specified
"""
import os
from typing import List

from databaser.data_model import DataModel
from databaser.engine.engine import DatabaseEngine
from databaser.engine.result import ExecutionResult
from databaser.pgsql import TableStructure, DatabaseStructure
from databaser.transaction import Transaction

from config import conn_string
from src.data_model.author import Author
from src.data_model.book import Book
from src.data_model.cart import CartItem
from src.data_model.customer import Customer
from src.data_model.favorite import Favorite
from src.data_model.order import Order


def create_table(model: DataModel) -> ExecutionResult:
    sql = TableStructure("pgsql").create_table(model.table_name, model.fields, model.schema_name).get_sql()
    res = DatabaseEngine(**conn_string).execute(sql)
    return res


tables: List[DataModel] = [
    Author(),
    Book(),
    Customer(),
    Order(),
    CartItem(),
    Favorite(),
]


def drop_table(model: DataModel):
    sql = TableStructure("pgsql").drop_table(model.table_name, if_exists=True).get_sql()
    res = DatabaseEngine(**conn_string).execute(sql)
    return res


def drop_database(database: str):
    sql = DatabaseStructure("pgsql").drop_database(database).get_sql()

    res = DatabaseEngine(**conn_string).execute(sql, transaction=False)
    return res


def create_local_functions():
    pathname = os.path.join(os.path.dirname(__file__), 'database_functions')

    create_functions = Transaction(conn_string)

    for function in os.listdir(pathname):
        print("Function Filename:", function)
        with open(os.path.join(pathname, function), 'r') as f:
            print("Function:", function)
            create_functions.add(f.read())

    create_functions.commit()


def run(postgres_config: dict):
    if int(postgres_config['drop_database']) > 0:
        print(("-"*10), "DROP Database", ("-"*10))
        drop_database(
            conn_string['database']
        )

    if int(postgres_config['drop_tables']) > 0:
        print(("-"*10), "DROP TABLES", ("-"*10))
        for table in reversed(tables):
            drop_table(table)

    for table in tables:
        print("Create Table:", table.table_name)
        create_table(table)

    create_local_functions()

