import React from 'react';
import { Redirect, Route, Switch } from 'react-router-dom';
import Navigation from './Components/navigation'
import Overview from './Components/overview'
import Sources from './Components/sources'
import AboutProject from './Components/about_project'

function App() {
    return (
        <div className="App">
        <header className="App-header">
            <Navigation/>
        </header>
        <Switch>
            <Redirect from="/" to="/overview" exact />
            <Route path="/overview" component={Overview} exact />
            <Route path="/sources" component={Sources} exact />
            <Route path="/project" component={AboutProject} exact />
        </Switch>
        </div>
    );
}

export default App;
