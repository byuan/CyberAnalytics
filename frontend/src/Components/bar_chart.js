import React from 'react';
import {Bar} from 'react-chartjs-2';


class BarChart extends React.Component {

    render() {
        return (
            <div>
                <Bar
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
                            },
                            scaleLabel: {
                                display: true,
                                labelString: this.props.ylabel
                            }
                        }]
                    }
                }}
                />
            </div>
        )
    }
}

export default BarChart;