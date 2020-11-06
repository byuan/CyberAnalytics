import React from 'react';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import NavDropdown from 'react-bootstrap/NavDropdown'


class Navigation extends React.Component {
    render() {
        return (
            <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
                <Navbar.Brand href="/overview">Cyber Thermometer</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="mr-auto">
                    <Nav.Link href="/overview">Overview</Nav.Link>
                    <NavDropdown title="Analysis" id="collapsible-nav-dropdown">
                        <NavDropdown.Item href="/articles/threatpost">Threatpost</NavDropdown.Item>
                        <NavDropdown.Item>Hacker News</NavDropdown.Item>
                        <NavDropdown.Divider />
                        <NavDropdown.Item href="/trending">Google Trending</NavDropdown.Item>
                        <NavDropdown.Divider />
                        <NavDropdown.Item>Dashboards</NavDropdown.Item>
                    </NavDropdown>
                    <Nav.Link href="/sources">Sources</Nav.Link>
                    </Nav>
                    <Nav>
                    <Nav.Link href="/project">About Our Project</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        )
    }
}

export default Navigation;