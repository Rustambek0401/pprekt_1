import psycopg2 as psql
import os
from dotenv import load_dotenv
load_dotenv()
class DataBase:
    @staticmethod
    def datbase(query, type):
        postgres = psql.connect(
        database=os.getenv('db_name'),
        host = os.getenv('db_host'),
        user = os.getenv('db_user'),
        password = os.getenv('db_parol')
        )
        corsor = postgres.cursor()
        corsor.execute(query)
        Type = ['insert','delete','drop','updata']
        if type in Type:
            postgres.commit()
            if type == 'insert':
                return "INSERT"
            elif type == "delete":
                return "DELETE"
            elif type == 'drop':
                return "DROP"
            elif type == "updata":
                return "UPDATA"
        else:
            return corsor.fetchall()