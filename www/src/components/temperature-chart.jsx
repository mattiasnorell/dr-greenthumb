/*global google*/ 

import React, {Component} from 'react';

export default class TemperatureChart extends Component {

    state = { data: [] }

    async componentDidMount(){
        
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