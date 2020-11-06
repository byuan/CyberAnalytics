import React from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import LineGraph from './line_graph'
import DoughnutChart from './donut_chart'
import RadarChart from './radar_chart'
import './dashboard.css'

class AnalysisThreatpost extends React.Component {

    async keywordAnalysis(n_days) {
        const res = await fetch(`http://192.168.204.54:5000/analysis/keywordsByDay?days=${n_days}`);
        return res.json();
    }

    render() {
        return (
            <Container>
                <Row>
                    <Col>
                        <LineGraph
                            get_data={this.keywordAnalysis}
                            count_days={30}
                            title='Trends by Keyword Score'
                            ylabel='Keyword Score'
                        />
                    </Col>
                </Row>
                <Row>
                    <Col className='dashboard-col'>
                        <DoughnutChart
                            get_data={this.keywordAnalysis}
                            count_days={1}
                            title='Todays Keyword Score Breakdown'
                        />
                    </Col>
                    <Col className='dashboard-col'>
                        <RadarChart
                            get_data={this.keywordAnalysis}
                            count_days={7}
                            title='Keyword Score Sums this Week'
                        />
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default AnalysisThreatpost;