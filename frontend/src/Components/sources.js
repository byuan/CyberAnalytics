import React from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import threatpost_logo from '../Images/threatpost_logo.png'
import './sources.css'

class Sources extends React.Component {
    render() {
        return (
            <Container>
                <Col className='source-col'>
                    <h3>Cybersecurity News</h3>
                    <h4>1. <a href="https://threatpost.com/" target="_blank">Threatpost</a> </h4>
                    <img src={threatpost_logo} alt="Logo"/>
                    <p>
                    Threatpost is an independent news site focused heavily in Cybersecurity and 
                    the Tech Industry. They post multiple original articles which are extremely 
                    relevant each day and are widely known and respected within the Cybersecurity 
                    Industry. We are currently scraping the articles within the Malware and 
                    Vulnerability sections of the site as we identified these as being the most 
                    relevant to users.
                    </p>
                </Col>
            </Container>
        )
    }
}

export default Sources;