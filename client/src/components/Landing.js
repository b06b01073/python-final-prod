import { useState, useEffect, useRef } from "react";
import Search from "./Search";
import { Container, Row, Col, ListGroup, Modal, Button } from "react-bootstrap";

const Landing = () => {
  const textMiddle = {
    textAlign: "center",
  };

  const imgStyle = {
    height: "40%",
    width: "40%",
  };
  return (
    <>
      <div className="landing-page">
        <Container className="form-container">
          <Row className="justify-content-md-center">
            <Col xs lg="10">
              <Search />
            </Col>
          </Row>
        </Container>
      </div>
      <br />
      <br />
      <Container style={textMiddle}>
        <h2>Source Data</h2>
        <img
          style={imgStyle}
          src="https://nc.iucnredlist.org/redlist/news_snippets/images/1536919087-IUCN_Red_List.jpg"
          alt="redlist icon"
        />
      </Container>
      <br />
    </>
  );
};

export default Landing;
