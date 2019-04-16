import React, {Component} from 'react';

export default class TemperatureChart extends Component {

    render() {
        return(

                <div className="gadget-content">
                    <div className="gadget-info-tab">
                        <div className="temperature">12&deg;</div>
                        <div className="description">Innetemp</div>
                        
                        <table>
                            <tbody>
                                <tr>
                                    <td>14:25</td>
                                    <td>15&deg;</td>
                                </tr>
                                <tr>
                                    <td>14:25</td>
                                    <td>15&deg;</td>
                                </tr>
                                <tr>
                                    <td>14:25</td>
                                    <td>15&deg;</td>
                                </tr>
                                <tr>
                                    <td>14:25</td>
                                    <td>15&deg;</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
        )
    }
}