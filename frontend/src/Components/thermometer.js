import React from 'react';
import Slider from '@material-ui/core/Slider';
import { createMuiTheme } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';

const levels = [
    {
        value: 0,
        label: 'Low'
    },
    {
        value: 20,
        label: 'Guarded'
    },
    {
        value: 40,
        label: 'Elevated'
    },
    {
        value: 60,
        label: 'High'
    },
    {
        value: 80,
        label: 'Severe'
    }
];

class Thermometer extends React.Component {
    state = {
        threat_level: 33
    };
    

    muiTheme = () => {
        var colors = {}
        switch (true) {
            case ( this.state.threat_level <= 20):
                colors = {
                    thumb: 'green',
                    track: 'green',
                    rail: 'gray',
                    valueLabelDisplay: 'black'
                };
                break;
            case ( this.state.threat_level <= 40):
                colors = {
                    thumb: 'blue',
                    track: 'blue',
                    rail: 'gray',
                    valueLabelDisplay: 'black'
                };
                break;
            case ( this.state.threat_level <= 60):
                colors = {
                    thumb: 'yellow',
                    track: 'yellow',
                    rail: 'gray',
                    valueLabelDisplay: 'black'
                };
                break;
            case ( this.state.threat_level <= 80):
                colors = {
                    thumb: 'orange',
                    track: 'orange',
                    rail: 'gray',
                    valueLabelDisplay: 'black'
                };
                break;
            case ( this.state.threat_level <= 100):
                colors = {
                    thumb: 'red',
                    track: 'red',
                    rail: 'gray',
                    valueLabelDisplay: 'black'
                };
        };
        return createMuiTheme({
        overrides:{
            MuiSlider: {
                thumb:{
                    color: colors.track,
                },
                track: {
                    color: colors.thumb
                },
                rail: {
                    color: colors.rail
                },
                valueLabel: {
                    color: 'gray'
                }
            }
        }
        });
    }

    handleChange = (event, value) => {
        this.setState({
            threat_level: value
        })
    }

    render() {
        return (
            <ThemeProvider theme={this.muiTheme()}>
                <Slider
                    //disabled
                    color='primary'
                    defaultValue={this.state.threat_level}
                    aria-labelledby="disabled-slider"
                    onChange={this.handleChange}
                    valueLabelDisplay="on"
                    marks={levels}
                />
            </ThemeProvider>
            
        )
    }
}

export default Thermometer;