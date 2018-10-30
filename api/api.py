import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Dr Greenthumb API</h1>'''


@app.route('/api/v1/sensors/', methods=['GET'])
def api_all():
    conn = sqlite3.connect('../db/greenhouse.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    sensors = cur.execute('SELECT * FROM Sensors;').fetchall()

    return jsonify(sensors)

@app.route('/api/v1/sensors/', methods=['GET'])
def api_sensors():
    
    conn = sqlite3.connect('../db/greenhouse.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    sensors = cur.execute('SELECT * FROM Sensors;').fetchall()

    return jsonify(sensors)

@app.route('/api/v1/sensors/<sensorid>', methods=['GET'])
def api_sensor(sensorid):
    
    conn = sqlite3.connect('../db/greenhouse.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    query = "SELECT * FROM Sensors where SensorId = '%s'" % (sensorid)
    sensors = cur.execute(query).fetchall()

    return jsonify(sensors)

@app.route('/api/v1/sensors/<sensorid>/data', methods=['GET'])
def api_sensor_data_read(sensorid):
    skip = request.args.get('skip', default = 0, type = int)
    take = request.args.get('take', default = 10, type = int)

    conn = sqlite3.connect('../db/greenhouse.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    sensors = cur.execute('''SELECT * FROM SensorData where SensorId = ? LIMIT ? OFFSET ?''', (sensorid, take,skip)).fetchall()

    return jsonify(sensors)

@app.route('/api/v1/sensors/<sensorid>/data', methods=['POST'])
def api_sensor_data_save(sensorid):
    val = request.json['value']
    conn = sqlite3.connect('../db/greenhouse.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    query = "INSERT INTO SensorData (SensorId, Datetime, SensorValue) VALUES(?,datetime('now','localtime'),?)"
    cur.execute(query,(sensorid, val))

    return jsonify("ok")


@app.route('/api/v1/sensors/type/<sensortype>', methods=['GET'])
def api_sensortype(sensortype):
    
    conn = sqlite3.connect('../db/greenhouse.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    sensors = cur.execute('''SELECT * FROM Sensors where SensorType = ?''', (sensortype,)).fetchall()

    return jsonify(sensors)

@app.route('/api/v1/log', methods=['POST'])
def api_log_save():
    val = request.json['message']

    conn = sqlite3.connect('../db/greenhouse.db')
    cur = conn.cursor()
   
    query = "INSERT INTO Logs (DateTime, Message) VALUES(datetime('now','localtime'),?)"
    cur.execute(query,(val,))

    return jsonify({'status':200})

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()