import React from 'react';
import {Doughnut} from 'react-chartjs-2';


class DoughnutChart extends React.Component {

    render() {
        return (
            <div>
                <Doughnut
                data={this.props.data}
                options={{
                    title:{
                        display:true,
                        text:this.props.title,
                        fontSize:20
                    },
                    legend:{
                        display:true,
                        position:'right'
                    }
                }}
                />
            </div>
        )
    }
}

export default DoughnutChart;