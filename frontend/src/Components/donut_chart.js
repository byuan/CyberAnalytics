import React from 'react';
import {Doughnut} from 'react-chartjs-2';


class DoughnutChart extends React.Component {
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
        var labels = [];
        var data =  [];
        var color = [];
        Object.keys(dataset).map((label) => {
            labels.push(label);
            data.push(dataset[label]);
            color.push('#'.concat(Math.floor(Math.random()*16777215).toString(16)));
        });

        const donut_data = {
            labels: labels,
            datasets: [
                {
                backgroundColor: color,
                label: 'Keywords',
                data: data
                }
            ]
        };

        this.setState({dataset: donut_data});
    }

    render() {
        return (
            <div>
                <Doughnut
                data={this.state.dataset}
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