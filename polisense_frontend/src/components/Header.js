import React from 'react'
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';

export default class Header extends React.Component {
    constructor(props) {
      super(props);
  
      this.toggle = this.toggle.bind(this);
      this.state = {
        isOpen: false
      };
    }
    toggle() {
      this.setState({
        isOpen: !this.state.isOpen
      });
    }
    render() {
      return (
        <div>
          <Navbar style={{backgroundColor: '#000000'}} light expand="md">
            <NavbarBrand className="text-danger" href="/">PoliSense</NavbarBrand>
            <NavbarToggler onClick={this.toggle} />
            <Collapse isOpen={this.state.isOpen} navbar>
              <Nav className="ml-auto" navbar>
                <NavItem>
                  <NavLink  className="text-warning"  href="/">Dashboard</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink className="text-warning" href="/placeholder1">Placeholder1</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink  className="text-warning" href="/placeholder2">Placeholder2</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink className="text-warning" href="https://github.com/bmolina-nyc/PoliSense">GitHub</NavLink>
                </NavItem>
              
              </Nav>
            </Collapse>
          </Navbar>
        </div>
      );
    }
  }



