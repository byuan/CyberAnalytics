import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Navigation from './Components/navigation'
import Overview from './Components/overview'
import Sources from './Components/sources'

function App() {
    return (
        <div className="App">
        <header className="App-header">
            <Navigation/>
        </header>
        <Switch>
            <Route path="/home" component={Overview} exact />
            <Route path="/sources" component={Sources} exact />
        </Switch>
        </div>
    );
}

export default App;
