import React, {Component} from 'react';

export default class Log extends Component {

    state = { data: [] };

    async componentDidMount(){
        const result = await this.getData();
        this.setState({data: result});

        setInterval(async () => {
            const result = await this.getData();
            this.setState({data: result});
        }, 60000);
    }

    async getData(){
        return fetch('http://127.0.0.1:5000/api/v1/log?take=10').then(response => response.json());
    }

    render() {
        return(

                <div className="gadget-content">
                    <div className="gadget-info-tab">
                        <table>
                            <tbody>
                                {this.state.data.map((value, index) => {
                                    return <tr key={index}>
                                        <td>{value.DateTime}</td>
                                        <td>{value.Message}</td>
                                    </tr>
                                })}
                            </tbody>
                        </table>
                    </div>
                </div>

        )
    }
}