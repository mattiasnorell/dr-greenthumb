import React, {Component} from 'react';
import Sensor from './sensor';

export default class Moisture extends Component {

    state = { sensors: [] };

    async componentDidMount(){
        const sensors = await fetch("http://127.0.0.1:5000/api/v1/sensors/type/moisture").then(response => response.json())

        this.setState({sensors: sensors});
    }

    render() {
        return(
            <div className="gadget-content">
          
                {this.state.sensors.map((sensor, index) => {
                return <div key={index} className="gadget-info-tab">
                    <Sensor sensorId={sensor.Id} sensorName={sensor.SensorName} />
                </div>
                })}
            </div>
        )
    }
}