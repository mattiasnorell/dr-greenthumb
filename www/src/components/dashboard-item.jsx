
import React, {Component} from 'react';
import Humidity from './humidity';
import HumidityChart from './humidity-chart';
import Log from './log';
import Temperature from './temperature';
import TemperatureChart from './temperature-chart';
import Light from './light';
import Moisture from './moisture';
import WaterFlow from './water-flow';
import WaterLevel from './water-level';
import Info from './info';

export default class DashboardItem extends Component {

    constructor(props){
        super(props);
        this.state = { data: [] };
    }

    render() {
        const components = {
            Humidity,
            HumidityChart,
            Log,
            Temperature,
            TemperatureChart,
            Light,
            WaterFlow,
            Moisture,
            WaterLevel,
            Info
        }

        let Module = this.props.widget;

        if(!components[Module]){
            return('');
        }

        const $component = components[Module];

        return (
        <div className={"gadget gadget-size-" + this.props.size + " gadget-theme-"+ this.props.theme+ " gadget-id-" +this.props.id + " gadget-name-" + this.props.widget.toLowerCase()}>
            
            {
                this.props.persistent === 0 && 
                <div className="gadget-header">
                    {this.props.title}
                </div>
            }

            <$component/>                  
        </div>
        )
    }
}