import React from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import BarChart from './bar_chart'
import LineGraph from './line_graph'
import DoughnutChart from './donut_chart'
import RadarChart from './radar_chart'
import './dashboard.css'

class GoogleTrends extends React.Component {

    async getGoogleTrends(n_days) {
        const res = await fetch(`http://192.168.204.54:5000/googleTrends`);
        return res.json();
    }

    render() {
        return (
            <Container fluid={true}>
                <Col xs={{ span:10, offset:1}}>
                    <LineGraph
                        get_data={this.getGoogleTrends}
                        title='Keyword Google Trends'
                        ylabel='Percentage'
                    />
                </Col>
            </Container>
        )
    }
}

export default GoogleTrends;