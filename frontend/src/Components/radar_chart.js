import React from 'react';
import {Radar} from 'react-chartjs-2';


class RadarChart extends React.Component {
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
        delete json_data['labels']

        var dataset = {}

        Object.keys(json_data).map((keyword) => {
            json_data[keyword].map((counts) => {
                if (typeof dataset[keyword] === 'undefined') {
                    dataset[keyword] = counts['y'];
                }
                else {
                    dataset[keyword] += counts['y'];
                }
            });
        });

        // TODO- update this single loop to build labels and data array
        const labels = Object.keys(dataset);
        const data = Object.keys(dataset).map((label) => {
            return dataset[label];
        });
        
        const radar_data = {
            labels: labels,
            datasets: [
                {
                backgroundColor: [
                    'rgba(75,192,192,1)',
                ],
                label: 'Keywords',
                data: data
                }
            ]
        }

        this.setState({dataset: radar_data})
    }

    render() {
        return (
            <div>
                <Radar
                data={this.state.dataset}
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
                }}
                />
            </div>
        )
    }
}

export default RadarChart;