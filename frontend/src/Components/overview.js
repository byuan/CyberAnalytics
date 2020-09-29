import React from 'react';
import Jumbotron from 'react-bootstrap/Jumbotron'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Thermometer from './thermometer'

class Overview extends React.Component {
    render() {
        return (
            <Jumbotron fluid>
                <Container>
                    <Row className="justify-content-md-center">
                        <h3>Current Threat Level</h3>
                    </Row>
                    <Row
                        className="justify-content-md-center"
                        style={{padding:'40px 20px 10px 20px'}}
                    >
                        <Col xs={9} >
                            <Thermometer/>
                        </Col>
                    </Row>
                </Container>
            </Jumbotron>
        )
    }
}

export default Overview;