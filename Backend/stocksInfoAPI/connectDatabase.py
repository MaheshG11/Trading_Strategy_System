import psycopg2
import os
import dotenv

dotenv.load_dotenv()


def conn(databaseName: str, port: int):
    return psycopg2.connect(
        database=databaseName,
        user=os.getenv(f"PSQLuser"),
        host="localhost",
        password=os.getenv(f"PSQLPassword"),
        port=port,
    )


class connectDatabase:
    def connect(databaseName: str, port: int = 5432):
        databaseName = databaseName.lower()
        try:
            db = conn(databaseName, port)
            db.autocommit = True
            return db
        except:
            try:
                db: psycopg2.extensions.connection
                db = conn("postgres", port=port)
                db.autocommit = True
                cur = db.cursor()
                query = f"CREATE DATABASE {databaseName};"
                cur.execute(query)
                db.commit()
                db.close()
                db = conn(databaseName, port)
                db.autocommit = True
                return db

            except Exception as e:
                print("Error: ", e)
