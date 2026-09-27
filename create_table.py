import psycopg2
from config import load_config

def create_tables():
    config = load_config()
    commands = (
        """
        CREATE TABLE IF NOT EXISTS products (
           id BIGINT NOT NULL PRIMARY KEY,
           price NUMERIC ,
           name VARCHAR(255) ,
           url_key VARCHAR(255),
           images_url TEXT, 
           description TEXT
        )
    """,
    )
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    


if __name__ == '__main__':
    create_tables()