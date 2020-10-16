import React from 'react';
import {Radar} from 'react-chartjs-2';


class RadarChart extends React.Component {

    render() {
        return (
            <div>
                <Radar
                data={this.props.data}
                options={{
                    title:{
                        display:true,
                        text:this.props.title,
                        fontSize:20
                    },
                    legend:{
                        display:false,
                        position:'right'
                    },
                    scales:{
                        yAxes:[{
                            ticks:{
                                beginAtZero: true
                            }
                        }]
                    }
                }}
                />
            </div>
        )
    }
}

export default RadarChart;