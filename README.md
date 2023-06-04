# Pre-requisites
1- Python 3.5 or higher
2- Postgres 14 or higher

# Installation
1- Clone the repository
```git clone https://github.com/Book-Store-Grad/bookstore-api.git```

2- Create a new Database in Postgres

3- change the config.ini file with your database credentials
    3a- change the initiate_db param to 1 to create the tables

4- run the following command to install the dependencies
```pip install -r requirements.txt```

5- Run the following command to start the server
```python main.py```