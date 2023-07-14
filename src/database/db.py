import psycopg2
from psycopg2 import DatabaseError
#from decouple import config

SECRET_KEY='P4ASSWORD'
DB_HOST='localhost'    
DB_USER='postgres'
DB_PASSWORD='postgres'
DB_DATABASE='postgis_project'
DB_PORT=5432

def get_connection(): 
    try:
        return psycopg2.connect(database=DB_DATABASE, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    except DatabaseError as ex:
        raise ex


#CREACION DE BASE DE DATOS A POSTGRESQL  

#     cursor = conn.cursor()

#     cursor.execute('''
#             CREATE TABLE IF NOT EXISTS weather_stations (
#                 id SERIAL PRIMARY KEY,
#                 name VARCHAR(100) NOT NULL,
#                 location GEOMETRY(POINT, 4326) NOT NULL
#             )
#         ''')
#     cursor.execute('''
#             CREATE TABLE IF NOT EXISTS weather_data (
#                 id SERIAL PRIMARY KEY,
#                 station_id INTEGER REFERENCES weather_stations(id) ON DELETE CASCADE,
#                 temperature FLOAT NOT NULL,
#                 humidity FLOAT NOT NULL,
#                 pressure FLOAT NOT NULL,
#                 timestamp TIMESTAMP NOT NULL
#             )
#         ''')
    
#     sql = '''
#         INSERT INTO weather_stations (name, location)
#         VALUES ('Estación 1', ST_SetSRID(ST_MakePoint(-99.145966, 19.432608), 4326)),
#             ('Estación 2', ST_SetSRID(ST_MakePoint(-98.224889, 19.033040), 4326)),
#             ('Estación 3', ST_SetSRID(ST_MakePoint(-99.139238, 19.427053), 4326));
#         '''
#     cursor.execute(sql)

#     data = '''
#         INSERT INTO weather_data (station_id, temperature, humidity, pressure, timestamp)
#         VALUES (1, 24.5, 0.6, 1013.4, '2023-03-19 10:00:00'),
#             (1, 25.1, 0.7, 1012.8, '2023-03-19 11:00:00'),
#             (2, 22.8, 0.5, 1015.2, '2023-03-19 10:00:00'),
#             (2, 23.3, 0.6, 1015.6, '2023-03-19 11:00:00'),
#             (3, 26.2, 0.8, 1011.2, '2023-03-19 10:00:00'),
#             (3, 25.9, 0.7, 1011.6, '2023-03-19 11:00:00'),
#             (1, 23.9, 0.6, 1012.2, '2023-03-19 12:00:00'),
#             (1, 24.6, 0.5, 1011.7, '2023-03-19 13:00:00'),
#             (1, 23.3, 0.7, 1010.5, '2023-03-19 14:00:00'),
#             (2, 22.4, 0.4, 1014.3, '2023-03-19 12:00:00'),
#             (2, 23.1, 0.5, 1014.7, '2023-03-19 13:00:00'),
#             (2, 22.8, 0.4, 1014.1, '2023-03-19 14:00:00'),
#             (3, 24.8, 0.6, 1012.9, '2023-03-19 12:00:00'),
#             (3, 25.5, 0.7, 1012.4, '2023-03-19 13:00:00'),
#             (3, 25.2, 0.6, 1012.1, '2023-03-19 14:00:00');
#         '''
#     cursor.execute(data)

#     conn.commit()

# except Exception as error:
#     print("error:", error)
# finally:
#     if cursor is not None: 
#         cursor.close()
#     if conn is not None: 
#         conn.close() 