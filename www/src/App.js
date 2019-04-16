import React, { Component } from 'react';
import DashboardItem from './components/dashboard-item';

import './App.scss';

class App extends Component {
  state = { widgets: []}
  
  async componentDidMount(){
       
    const widgets = await fetch("http://127.0.0.1:5000/api/v1/widgets/").then(response => response.json())

    this.setState({widgets: widgets});
  }

  render() {
    const { widgets } = this.state;
    
    return (
      <div className="App">
          <header className="App-header">
            <h1>Dr Greenthumb</h1>
          </header>
          
          { widgets.map((item, i) => {
            return <DashboardItem key={i} widget={item.Widget} title={item.Title} size={item.Size} theme={item.Theme} id={item.Id} />
          }) }

      </div>
    );
  }
}

export default App;
