import React from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import BarChart from './bar_chart'
import LineGraph from './line_graph'
import DoughnutChart from './donut_chart'
import RadarChart from './radar_chart'
import './dashboard.css'

const keywords_breakdown = {
    labels: ['Ransomware', 'Breach', 'Exploit', 'Malware',
             'Virus', 'Worm', 'Covid-19'],
    datasets: [
      {
        backgroundColor: [
            'rgba(29, 195, 187, 1)',
            'rgba(129, 29, 195, 1)',
            'rgba(195, 29, 29, 1)',
            'rgba(195, 121, 29, 1)',
            'rgba(60, 195, 29, 1)',
            'rgba(40, 29, 195, 1)',
            'rgba(190, 195, 29, 1)',
        ],
        label: 'Keywords',
        data: [28, 15, 8, 13, 6, 4, 26]
      }
    ]
  }

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

const keyword_trends = {
    labels: ['10/10', '10/11', '10/12', '10/13',
             '10/14', '10/15', '10/16'],
    datasets: [
      {
        label: 'Ransomware',
        backgroundColor: 'rgba(75,192,192,1)',
        fill: false,
        borderColor: 'rgba(75,192,192,1)',
        borderWidth: 1,
        data: [8, 5, 9, 3, 14, 16, 13]
      },
      {
        label: 'Breach',
        backgroundColor: 'rgba(230,59,59,1)',
        fill: false,
        borderColor: 'rgba(230,59,59,1)',
        borderWidth: 1,
        data: [2, 4, 3, 6, 9, 10, 7]
      }
    ]
  }

const radar_data = {
    labels: ['Ransomware', 'Breach', 'Exploit', 'Malware',
             'Virus', 'Worm', 'Covid-19'],
    datasets: [
      {
        borderColor: 'rgba(29, 195, 187, 1)',
        borderWidth: 1,
        label: 'Keywords',
        data: [28, 15, 8, 13, 6, 4, 26]
      }
    ]
  }

class OverviewDashboard extends React.Component {

    componentDidMount() {
        fetch("http://localhost:5000/keywords")
            .then(res => res.json())
            .then((result) => {
                console.log(result)
            })
            .catch((error) => {
                console.log(error)
            })
    }
    render() {
        return (
            <Container>
                <Row>
                    <Col className='dashboard-col'>
                        <DoughnutChart
                            data={keywords_breakdown}
                            title='Todays Keyword Breakdown'
                        />
                    </Col>
                    <Col className='dashboard-col'>
                        <LineGraph
                            data={keyword_trends}
                            title='Trends by Keyword'
                        />
                    </Col>
                </Row>
                <Row>
                    <Col className='dashboard-col'>
                        <BarChart
                            data={keywords_per_month}
                            title='Keywords per Month'
                        />
                    </Col>
                    <Col className='dashboard-col'>
                        <RadarChart
                            data={radar_data}
                            title='Radar Example'
                        />
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default OverviewDashboard;