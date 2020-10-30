import React from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import BarChart from './bar_chart'
import LineGraph from './line_graph'
import DoughnutChart from './donut_chart'
import RadarChart from './radar_chart'
import './dashboard.css'

const keywords_per_month = {
    labels: ['May', 'June', 'July', 'August',
             'September', 'October'],
    datasets: [
      {
        label: 'Keywords',
        backgroundColor: 'rgba(75,192,192,1)',
        borderColor: 'rgba(0,0,0,1)',
        borderWidth: 2,
        data: [267, 206, 176, 157, 348, 163]
      }
    ]
  }

class OverviewDashboard extends React.Component {

    async keywordAnalysis(n_days) {
        const res = await fetch(`http://192.168.202.233:5000/analysis/keywordsByDay?days=${n_days}`);
        return res.json();
    }

    render() {
        return (
            <Container>
                <Row>
                    <Col className='dashboard-col'>
                        <DoughnutChart
                            get_data={this.keywordAnalysis}
                            count_days={1}
                            title='Todays Keyword Score Breakdown'
                        />
                    </Col>
                    <Col className='dashboard-col'>
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
                        <BarChart
                            data={keywords_per_month}
                            title='Keyword Scores per Month (Example Data)'
                            ylabel='Keyword Score'
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

export default OverviewDashboard;