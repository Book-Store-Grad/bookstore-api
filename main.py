import os

import uvicorn

from config import system_environment
from server.application import app

import endpoints

if __name__ == '__main__':
    PARENT_DIR = os.getcwd()
    debug_mode = bool(int(system_environment('config.ini', 'env')['debug']))

    postgres = system_environment('config.ini', 'postgresql-server')
    postgres_config = system_environment('config.ini', 'postgresql_config')
    if debug_mode:
        print("Postgres", postgres)

    print("Init all database tables")
    if int(postgres_config['initiate_db']) > 0:
        from src.core.database.factory import run
        run(postgres_config)

    port = int(os.environ.get("PORT", 8005))

    uvicorn.run(app, host="0.0.0.0", port=port)
