import React from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import project_diagram from '../Images/project_diagram.png'
import scrapy_logo from '../Images/scrapy_logo.png'
import database_schema from '../Images/database_schema.png'
import analysis_process from '../Images/analysis_process.png'
import flask_logo from '../Images/flask_logo.png'
import react_logo from '../Images/react_logo.png'

import './about_project.css'

class AboutProject extends React.Component {
    render() {
        return (
            <Container>
                <Row className='about-row'>
                    <Col>
                        <h3>Overview</h3>
                        <Row xs={7}><img src={project_diagram} alt="Logo"/></Row>
                    </Col>
                </Row>
                <Row className='about-row'>
                    <Col>
                        <h3>Data Collection Module</h3>
                        <img src={scrapy_logo} alt="Logo" />
                        <p>
                            The first step to building our project was to determine a <a href="/sources"> source </a> 
                            to acquire frequent data from. For the first source, we opted for a Cybersecurity News 
                            site. Once this was decided, we then needed a way to break down the website in a way 
                            that was clean, efficient, and consistently grabbed the data we wanted to collect. To 
                            handle this task, we opted to use the Python Scrapy Library. The script parses through 
                            the URL, Title, Date, and article text for each article being evaluated. Once this data 
                            has been properly parsed, it is then compared against articles already in storage to 
                            prevent duplicates.
                        </p>
                    </Col>
                </Row>
                <Row className='about-row'>
                    <Col>
                        <h3>Data Storage Module</h3>
                        <p>
                            Once we had started to collect data, we needed a place to store it. For this we selected 
                            MySQL for its ability to store and serve large sets of data. Being a structured database, we 
                            needed to define how we would store data in a scalable way. Working together we created 
                            the following schema:
                        </p>
                        <img src={database_schema} alt="Logo" />
                        <p>
                            The above schema provided storage for any type of article from any source, allows us to add 
                            or disable keywords as needed, and allows us to break out the analysis of the articles into 
                            a separate module, which could expanded to provide deeper insights into the current data 
                            type.
                        </p>
                    </Col>
                </Row>
                <Row className='about-row'>
                    <Col>
                        <h3>Analysis Module</h3>
                        <Row xs={7}><img src={analysis_process} alt="Logo" /></Row>
                        <p>
                            To analyze the data that was submitted to the database, we first retrieve a list of keywords from 
                            the database and store them in our program. Then we parse the data input by the data collection 
                            portion and count the number of times each keyword is used in each article. Each keyword has a 
                            weight that is then multiplied to the count of each keyword. Once calculated, the program takes 
                            the article id, keyword id, keyword count, and weighted count and makes a new entry in our 
                            database. To weight each keyword, we based our logic on how general the term is and what is at 
                            risk. For example, a term such as 'malware' would be weighted lower than a term such as 'Magecart' 
                            or 'ransomware'. The reasoning is that 'malware' incorporates a wide spectrum of malicious programs 
                            that can be destructive but relatively harmless as well. A term like 'Magecart' that has been 
                            coined by the security community is known to steal and sell credit card data. All the while, 
                            'ransomware', although a broad term, is known for holding data ransom and costs companies a great 
                            deal more.
                        </p>
                    </Col>
                </Row>
                <Row className='about-row'>
                    <Col>
                        <h3>Visualization Module</h3>
                        <p>
                            To visualize our analytics we needed to create a website. Our primary goal for the website was for 
                            it to be modern and visually appealing while providing valuable insights into our data.
                        </p>
                        <h4>Backend</h4>
                        <img src={flask_logo} alt="Logo" />
                        <p>
                            We opted to build the backend of our website in Flask for several reasons. With the other modules 
                            being built in Python, it made sense to extend that to the website as well. In the future, this will 
                            allow us to implement these modules within the backend server, allowing the website to manage when 
                            these modules are executed. We selected Flask over other frameworks because of its wide use, 
                            community support, and ease to get started with.
                        </p>
                        <h4>Frontend</h4>
                        <img src={react_logo} alt="Logo" />
                        <p>
                            For the frontend, we chose to use React, a Javascript framework for building user interfaces. This 
                            was so that we could achieve our goal of a visually attractive website. React is a library 
                            which is made up of "components". Leveraging open source components from other libraries, mainly
                            React Bootstrap and Chart.js, we were able to quickly build a website that met our goals.
                        </p>
                    </Col>
                </Row>
                <Row/>
            </Container>
        )
    }
}

export default AboutProject;