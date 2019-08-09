import React, {Component} from 'react';
import Schedule from './schedule';

export default class Info extends Component {

    state = { tabIndex: 0, settings: null};

    async componentDidMount(){
       const settings = await fetch('http://127.0.0.1:5000/api/v1/settings/getactive').then(response => response.json());

       this.setState((state) => ({...state, settings: settings}));
    }

    componentDidUpdate(){
        console.log("nu")
    }

    tabSelect(index){
        this.setState((state) => ({...state, tabIndex: index}))
    }

    render() {
        const {settings, tabIndex} = this.state;

        return(
            <div>
                <div className={`gadget-info-tab ${tabIndex === 0 ? 'active':''}`} >
                    {settings ? settings.Description : ''}
                </div>

                <div className={`gadget-info-tab ${tabIndex === 1 ? 'active':''}`} >
                    <Schedule id={settings ? settings.Id : null}></Schedule>
                </div>

                <div className={`gadget-info-tab ${tabIndex === 2 ? 'active':''}`} >
                    <img src="https://www.telegraph.co.uk/content/dam/Gardening/11sept/Eco-shed.jpg" alt="Greenhouse overview" />
                </div>

                <div className={`gadget-info-tab ${tabIndex === 3 ? 'active':''}`} >
                    <h2>Inställningar</h2>
                </div>
        
                <div className="gadget-toggles">
                    <ul>
                        <li onClick={() => this.tabSelect(0)}>
                            <i className="fa fa-info-circle"></i>
                            <span>Info</span>
                        </li>
                        <li onClick={() => this.tabSelect(1)}>
                            <i className="fa fa-calendar"></i>
                            <span>Schema</span>
                        </li>
                        <li onClick={() => this.tabSelect(2)}>
                            <i className="fa fa-camera"></i>
                            <span>Bild</span>
                        </li>
                        <li onClick={() => this.tabSelect(3)}>
                            <i className="fa fa-cog"></i>
                            <span>Inställningar</span>
                        </li>
                    </ul>
                
                </div>
            </div>
        )
    }
}