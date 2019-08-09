
import React, {Component} from 'react';
import DashboardItem from './dashboard-item';

export default class Dashboard extends Component {

    state = { widgets: [] };

    async componentDidMount(){
       
        const widgets = await fetch("http://127.0.0.1:5000/api/v1/widgets/").then(response => response.json())
    
        this.setState({widgets: widgets});
      }

    render() {
        const { widgets } = this.state;

        return (
            <div>
                { widgets.map((item, i) => {
                    return <DashboardItem key={i} widget={item.Widget} persistent={item.Persistent} title={item.Title} size={item.Size} theme={item.Theme} multipage={item.Multipage} id={item.Id} />
                }) }
            </div>
        )
    }
}