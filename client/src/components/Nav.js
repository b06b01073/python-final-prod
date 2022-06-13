import React from "react";

import { Navbar, Nav as N, Container, Button } from "react-bootstrap";
import { Github } from "react-bootstrap-icons";

const Nav = () => {
  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="/">Group 1</Navbar.Brand>
          <N className="me-rl">
            <N.Link
              href="https://github.com/b06b01073/python-final"
              target="_blank"
            >
              <Button
                style={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  margin: "0px",
                }}
              >
                <Github /> Github
              </Button>
            </N.Link>
          </N>
        </Container>
      </Navbar>
    </>
  );
};

export default Nav;
