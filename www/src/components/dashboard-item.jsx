
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

export default class DashboardItem extends Component {

    state = { data: [] };

    async componentDidMount(){
        
    }

    // This is a dirty hack until i fix the database ids
    getModuleName(widgetName){
        widgetName = widgetName.charAt(0).toUpperCase() + this.props.widget.slice(1)
        
        const widgetNameSplit = widgetName.split('-');
        widgetName = widgetNameSplit.length > 1 ? widgetNameSplit[0] + widgetNameSplit[1].charAt(0).toUpperCase() + widgetNameSplit[1].slice(1) : widgetName;

        return widgetName;
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
            WaterLevel
        }

        let Module = this.getModuleName(this.props.widget);

        if(!components[Module]){
        return('');
        }

        const $component = components[Module];

        return (
        <div className={"gadget gadget-size-" + this.props.size + " gadget-theme-"+ this.props.theme+ " gadget-" +this.props.id}>
            <div className="gadget-header">{this.props.title}</div>
            <$component />                  
        </div>
        )
    }
}