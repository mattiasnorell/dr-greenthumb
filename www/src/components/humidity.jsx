import React, {Component} from 'react';

export default class Humidity extends Component {

    state = { data: [] };

    async componentDidMount(){
        const sensors = await fetch("http://127.0.0.1:5000/api/v1/sensors/type/humidity").then(response => response.json())

        const sensorData = [];

        for(let i = 0; i < sensors.length;i++){
            const sensor = sensors[i];
            const sensorModel = {
                name: sensor.SensorName,
                id: sensor.Id,
                currentValue: null,
                values: []
            };

            const data = await fetch(`http://127.0.0.1:5000/api/v1/sensors/${sensor.Id}/data?take=6`).then(response => response.json())

            console.log(data)
            sensorModel.currentValue = data[0];
            sensorModel.values = data.splice(1, data.length);

            sensorData.push(sensorModel);
            console.log(sensorModel)
        };

        this.setState({data: sensorData});

        console.log(sensorData)
    }

    render() {
        return(
                
            <div className="gadget-content">
                {this.state.data.map((sensor, index) => {
                return <div key={index} className="gadget-info-tab">
                    <div className="temperature">{sensor.currentValue? Math.round(sensor.currentValue.SensorValue) : ''}%</div>
                    <div className="description">{sensor.name}</div>
                    
                    <table>
                        <tbody>
                            {sensor.values.map((value, index) => {
                                return <tr key={index}>
                                    <td>{value.DateTime}</td>
                                    <td>{Math.round(value.SensorValue)}%</td>
                                </tr>
                            })}
                        </tbody>
                    </table>
                </div>
                })}
            </div>	
            
        )
    }
}