import React, { Component } from 'react';
import Dashboard from './components/dashboard';

import './App.scss';

class App extends Component {
  
  render() {
    
    return (
      <div className="App">
          <header className="App-header">
            <h1>Dr Greenthumb</h1>
          </header>
          
          <Dashboard></Dashboard>

      </div>
    );
  }
}

export default App;
