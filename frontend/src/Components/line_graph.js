import React from 'react';
import {Line} from 'react-chartjs-2';
import 'chartjs-adapter-moment';


class LineGraph extends React.Component {
    constructor() {
        super();
        this.state = {
            dataset: {},
        }
    }

    async componentDidMount() {
        const json_data = await this.props.get_data(this.props.count_days)
        this.generateData(json_data)
    }

    generateData = (json_data) => {
        var line_graph_data = {
            labels: json_data['labels'],
            datasets: []
        };
        
        delete json_data['labels']
        Object.keys(json_data).map((keyword) => {
            if (keyword !== 'labels') {
                const random_color = '#'.concat(Math.floor(Math.random()*16777215).toString(16))
                line_graph_data.datasets.push({
                    label: keyword,
                    backgroundColor: random_color,
                    fill: false,
                    borderColor: random_color,
                    borderWidth: 1,
                    data: json_data[keyword]
                });
            }
            return;
        });

        this.setState({dataset: line_graph_data})
    }

    render() {
        return (
            <div>
                <Line
                data={this.state.dataset}
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
                            },
                            scaleLabel: {
                                display: true,
                                labelString: this.props.ylabel
                            }
                        }],
                        xAxes: [{
                            type: 'time',
                            //distribution: 'series',
                            ticks: {
                                source: 'data',
                            },
                            time: {
                                unit: 'day',
                                parser: 'YYYY-MM-DD',
                                
                            },
                        }]
                    },
                    tooltips: {
                        mode: 'x'
                    }
                }}
                />
            </div>
        )
    }
}

export default LineGraph;