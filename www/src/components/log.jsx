import React, {Component} from 'react';

export default class Log extends Component {

    state = { data: [] };

    componentDidMount(){
        fetch('http://127.0.0.1:5000/api/v1/log?take=10')
        .then(response => response.json())
        .then(data => this.setState({data: data}))
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