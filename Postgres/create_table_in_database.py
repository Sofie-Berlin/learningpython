import psycopg2
from config import config


def create_tables(tablename, tablename2):
    """ create tables in the PostgreSQL database"""
    commands = (
        
        """
        CREATE TABLE """ + tablename + """ (
            id text,
            name text
        )
        """,
        """ CREATE TABLE """ + tablename2 + """ (
                id text,
                name text
                )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables("voegel","regenschirme")