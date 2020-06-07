import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component{

  constructor(){
    super();
    this.state = {
      meaningOfLife: 47
    }
  }

  increment = () => {
    this.setState(
      (prevState, prevProps) => {
       return {meaningOfLife: prevState.meaningOfLife + prevProps.increment}
      },
      () => console.log(this.state.meaningOfLife));
    console.log(this.state.meaningOfLife);
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            { this.state.meaningOfLife }
          </p>
          <button onClick={this.increment}>
            Update data
          </button>
        </header>
      </div>
    );
  }
}


export default App;
