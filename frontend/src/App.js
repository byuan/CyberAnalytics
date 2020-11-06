import React from 'react';
import { Redirect, Route, Switch } from 'react-router-dom';
import Navigation from './Components/navigation'
import Overview from './Components/overview'
import Sources from './Components/sources'
import AboutProject from './Components/about_project'
import GoogleTrends from './Components/google_trending'
import AnalysisThreatpost  from './Components/analysis_threatpost'

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
            <Route path="/trending" component={GoogleTrends} exact />
            <Route path="/articles/threatpost" component={AnalysisThreatpost} exact />
        </Switch>
        </div>
    );
}

export default App;
