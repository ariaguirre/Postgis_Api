from database.db import get_connection
from flask import Flask, jsonify, request
from .entities.Station import Station
import psycopg2


class StationModel():
     
    @classmethod
    def getStations(self):
        try: 
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('SELECT * FROM weather_stations')
            rows = cur.fetchall()
            cur.close()
            conn.close()
            
            results = []
            for row in rows:
                result = {
                    'id': row[0],
                    'name': row[1],
                    'location': row[2],
                }
                results.append(result)
            return results

        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def update_station(cls, station_id, updated_name, updated_latitude, updated_longitude):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE weather_stations SET name = %s, location = ST_SetSRID(ST_MakePoint(%s, %s), 4326) WHERE id = %s""", (updated_name, updated_longitude, updated_latitude, station_id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_station(cls, name, latitude, longitude):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO weather_stations (name, location) VALUES (%s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))""", (name, longitude, latitude))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_nearest(self, station):
        try: 
            lat = request.json['lat']
            lon = request.json['lon']            
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT ws.name AS station_name, wd.temperature, wd.humidity, wd.pressure, wd.timestamp FROM weather_stations AS ws INNER JOIN weather_data AS wd ON ws.id = wd.station_id WHERE ws.location <#> ST_SetSRID(ST_MakePoint(%s, %s), 4326) = (SELECT MIN(ws.location <#> ST_SetSRID(ST_MakePoint(%s, %s), 4326)) FROM weather_stations AS ws) ORDER BY wd.timestamp DESC LIMIT 1""", (lon, lat, lon, lat))

                result = cursor.fetchone()
                connection.commit()

            connection.close()
            if result is not None:
                station_name, temperature, humidity, pressure, timestamp = result
                response = {
                    'station_name': station_name,
                    'temperature': temperature,
                    'humidity': humidity,
                    'pressure': pressure,
                    'timestamp': timestamp
                }
                return jsonify(response)
            else:
                return jsonify({'message': 'No weather data found for the nearest station.'}), 404

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_station(self, station):
            try:
                connection = get_connection()

                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM weather_stations WHERE id = %s", (station.id,))
                    affected_rows = cursor.rowcount
                    connection.commit()

                connection.close()
                return affected_rows
            except Exception as ex:
                raise Exception(ex)