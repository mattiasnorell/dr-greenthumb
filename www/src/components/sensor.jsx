import React, {Component} from 'react';

export default class Sensor extends Component {

    state = { currentValue: null, history: [] };

    async componentDidMount(){
        if(!this.props.sensorId){
            return;
        }

        const data = await fetch(`http://127.0.0.1:5000/api/v1/sensors/${this.props.sensorId}/data?take=6`).then(response => response.json())
       
        this.setState({current: data[0], history: data.splice(1, data.length)});
    }

    render() {
        const {current, history} = this.state;

        return(
                
            <div>
                
                <div className="temperature">{current? Math.round(current.SensorValue) : ''}{this.props.valueToken}</div>
                <div className="description">{this.props.sensorName}</div>
                
                <table>
                    <tbody>
                        {history.map((value, index) => {
                            return <tr key={index}>
                                <td>{value.DateTime}</td>
                                <td>{Math.round(value.SensorValue)}%</td>
                            </tr>
                        })}
                    </tbody>
                </table>
            </div>        
            
        )
    }
}