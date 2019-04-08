import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import DashboardPage from '../components/DashboardPage';
import Header from '../components/Header';
import PlaceholderPage1 from '../components/PlaceholderPage1';
import PlaceholderPage2 from '../components/PlaceholderPage2';

const appRouter = () => (
    <BrowserRouter>
        <Header />
        <div>
            <Switch>
                <Route exact path="/" component={DashboardPage}></Route>
                <Route path="/placeholder1" component={PlaceholderPage1}></Route>
                <Route path="/placeholder2" component={PlaceholderPage2}></Route>
            </Switch>
        </div>
    </BrowserRouter>
)

export default appRouter