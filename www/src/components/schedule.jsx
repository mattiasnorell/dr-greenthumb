import React, {Component} from 'react';

export default class Schedule extends Component {
    state = { schedule: []};

    async componentDidMount(){
        if(!this.props.id){
            return;
        }

       this.loadSchedule();
    }

    async componentDidUpdate(oldProps){
        if(oldProps.id === this.props.id){
            return;
        }

        this.loadSchedule();
    }

    async loadSchedule(){
        const schedule = await fetch('http://127.0.0.1:5000/api/v1/schedule/' + this.props.id).then(response => response.json());

        this.setState({schedule: schedule});
    }

    render() {
        return(                
            <table>
                <tbody>
                    {this.state.schedule.map((item, index) => {
                        return <tr key={index}>
                            <td>{item.StartDate}</td>
                            <td className="text-right">{item.ItemName}</td>
                        </tr>
                    })}
                </tbody>
            </table>

        )
    }
}