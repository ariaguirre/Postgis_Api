from flask import Blueprint, jsonify, request
from models.entities.Station import Station
from models.StationModel import StationModel

main  = Blueprint('location_blueprint', __name__)

@main.route('/')
def get_stations():
    try: 
        stations = StationModel.getStations()
        return jsonify(stations)
    except Exception as ex: 
        return jsonify({'message': str(ex)}), 500
    
# 1. Crear una nueva estación meteorológica,dados su nombre y ubicación geoespacial (latitud y longitud);

@main.route('/add', methods=['POST'])
def add_station():
    try:
        name = request.json['name']
        latitude = request.json['latitude']
        longitude = request.json['longitude']

        affected_rows = StationModel.create_station(name, latitude, longitude)

        if affected_rows > 0:
            return jsonify({'message': 'Weather station created successfully'}), 201
        else:
            return jsonify({'message': 'Failed to create weather station'}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

# 2. Dada una ubicación por latitud-longitud, devolver el nombre de la estación meteorológica más cercana así como los datos más reciente registrados por esta

@main.route('/nearest/', methods=['POST'])
def nearest_station():
    try: 
        lat = request.json['lat']
        lon = request.json['lon']
        station = Station(id=None)
        result = StationModel.get_nearest(station)

        if result is not None: 
            return result
        else: 
            return jsonify({'message': 'No weather data found for the nearest station.'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500     


# 3. Actualizar los datos de una estación meteorológica existente (nombre y/o ubicación), proporcionando su identificador único y los nuevos datos a actualizar.

@main.route('/update/<int:station_id>', methods=['PUT'])
def update_station(station_id):
    try:
        updated_name = request.json['name']
        updated_latitude = request.json['latitude']
        updated_longitude = request.json['longitude']

        affected_rows = StationModel.update_station(station_id, updated_name, updated_latitude, updated_longitude)

        if affected_rows > 0:
            return jsonify({'message':'Weather station updated successfully'})
        else:
            return jsonify({'message': "No weather station updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    


# 4. Eliminar una estación meteorológica existente, proporcionando su identificador único.

@main.route('/delete/<id>', methods=['DELETE'])
def delete_station(id):
    try:
        station = Station(id)

        affected_rows = StationModel.delete_station(station)

        if affected_rows == 1:
            return jsonify(station.id)
        else:
            return jsonify({'message': "No station deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500