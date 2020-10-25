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
        const json_data = await this.props.get_data()
        this.generateData(json_data)
    }

    generateData = (json_data) => {
        console.log(json_data)

        var line_graph_data = {
            labels: json_data['labels'],
            datasets: []
        };
        
        delete json_data['labels']
        Object.keys(json_data).map((keyword) => {
            /**json_data[keyword].map((point) => {
                if (typeof point == 'object') {
                    point['x'] = Date.parse(point['x']);
                    console.log(point);
                }
                
            });*/
            console.log(keyword)
            console.log(json_data[keyword])
            if (keyword !== 'labels') {
                line_graph_data.datasets.push({
                    label: keyword,
                    backgroundColor: 'rgba(75,192,192,1)',
                    fill: false,
                    borderColor: 'rgba(75,192,192,1)',
                    borderWidth: 1,
                    data: json_data[keyword]
                });
            }
            return;
        });
        var filtered = line_graph_data.datasets.filter(function(el) {
            console.log(el)
            return typeof el == 'object';
        })
        console.log('line graph data')
        console.log(line_graph_data.datasets)
        this.setState({dataset: line_graph_data})
    }

    render() {
        //const dataset = this.generateData(this.props.get_data)
        console.log('component')
        console.log(this.state.dataset)
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