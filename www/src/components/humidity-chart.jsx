/*global google*/ 

import React, {Component} from 'react';

export default class HumidityChart extends Component {

    state = { data: [] }

    async componentDidMount(){
        const sensors = await fetch("http://127.0.0.1:5000/api/v1/sensors/type/humidity").then(response => response.json())
        const data = [];
        let sensorDataCount = 0;

        for(let i = 0; i < sensors.length; i++) {
            const sensor = sensors[i];
            const sensorResult = await fetch(`http://127.0.0.1:5000/api/v1/sensors/${sensor.Id}/data`).then(response => response.json())
            
            sensorDataCount = sensorResult.length;

            const sensorData = {id: sensor.Id, name: sensor.SensorName, sensorValues: []};

            for(let ii = 0; ii < sensorResult.length; ii++){
                const sensorDataItem = sensorResult[ii];
                sensorData.sensorValues.push({ timestamp: sensorDataItem.DateTime, value: sensorDataItem.SensorValue })
            }

            data.push(sensorData);
        };

        this.setState({data: data, valueCount: sensorDataCount});

        this.mapData();
    }
    
    mapData(){
        if(this.state.data == null){
            return;
        }

        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(() => {
            const rawChartData = ["{type: 'date', label: 'Tid'}"]
            
            this.state.data.forEach((sensor) => {
                rawChartData.push(sensor.name);
            });

           /* for(var i = 0; i < this.state.valueCount; i++){
                const tempData = [];
                tempData.push(this.state.data[0].sensorValues[i].timestamp);
                tempData.push(this.state.data[0].values[i].value);
               // tempData.push(this.state.data[1].values[i].value);

                rawChartData.push(tempData);
            }*/


            const data = google.visualization.arrayToDataTable([rawChartData]);

            var options = {
                hAxis: {
                    title: 'Tid',  
                    titleTextStyle: {
                        color: '#333'
                    }	    		
                },
                vAxis: {
                    minValue: 17
                },
                legend: 'top'
            };

            var chart = new google.visualization.AreaChart(document.getElementById('chart_temperature'));
            chart.draw(data, options);
        });
    }
    render() {
        return(

                <div className="gadget-content">
                    <div id="chart_temperature"></div>
                </div>	
        )
    }
}