import flask
from flask import request, jsonify
import sqlite3
from flask_cors import CORS
import operator
from flask import Response, escape

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    rules = []
    routes = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"/>'
    routes += '<h1 class="text-center">Dr Greenthumb API</h1><table class="table table-striped">'
    routes += '<tr><thead><th>Name</th><th>Methods</th><th>Route</th></thead></tr><tbody>'
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))

    sort_by_rule = operator.itemgetter(2)
    for endpoint, methods, rule in sorted(rules, key=sort_by_rule):
        route = '<tr><td>{:50s}</td><td>{:25s}</td><td>{}</td></tr>'.format(endpoint, methods, escape(rule))
        routes += route
    
    routes += "</tbody></table>"

    return Response(routes, mimetype="text/html")

@app.route('/api/v1/widgets/', methods=['GET'])
def api_widgets():
    conn = sqlite3.connect('../db/greenhouse.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    sensors = cur.execute('SELECT * FROM Widgets WHERE Active = 1 ORDER BY SortOrder;').fetchall()

    return jsonify(sensors)

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

@app.route('/api/v1/sensors/<int:sensorid>', methods=['GET'])
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

@app.route('/api/v1/log', methods=['GET'])
def api_log_get():
    
    skip = request.args.get('skip', default = 0, type = int)
    take = request.args.get('take', default = 10, type = int)

    conn = sqlite3.connect('../db/greenhouse.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    result = cur.execute('''SELECT * FROM Logs LIMIT ? OFFSET ?''', (take,skip)).fetchall()

    return jsonify(result)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()