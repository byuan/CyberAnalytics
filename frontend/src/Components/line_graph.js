import React from 'react';
import {Line} from 'react-chartjs-2';


class LineGraph extends React.Component {

    render() {
        return (
            <div>
                <Line
                data={this.props.data}
                options={{
                    title:{
                        display:true,
                        text:this.props.title,
                        fontSize:20
                    },
                    legend:{
                        display:true,
                        position:'top'
                    },
                    scales:{
                        yAxes:[{
                            ticks:{
                                beginAtZero: true
                            }
                        }]
                    },
                    tooltips: {
                        mode: 'index'
                    }
                }}
                />
            </div>
        )
    }
}

export default LineGraph;