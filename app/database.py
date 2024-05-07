# import psycopg2

# from utils.logging import get_logger


# logger = get_logger(__name__)


# try:
#     conn = psycopg2.connect(host='db', database='demo', user='user', password='pass')
#     conn.autocommit = True
# except:
#     logger.error("I am unable to connect to the database")

# table = 'mytable'

# with conn.cursor() as cur:
#     try:
#         cur.execute(f"CREATE TABLE IF NOT EXISTS {table} (my_id SERIAL PRIMARY KEY, my_string VARCHAR(255))")
#         cur.execute(f"INSERT INTO  {table} (my_string) VALUES ('MyTest') ON CONFLICT DO NOTHING")
#         cur.execute(f"SELECT * FROM {table}")
#         result = cur.fetchone()
#         logger.info(str(result))

#     except (Exception, psycopg2.DatabaseError) as error:
#         logger.error(error)
