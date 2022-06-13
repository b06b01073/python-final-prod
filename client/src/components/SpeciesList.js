import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { Container, ListGroup, Row, Col } from "react-bootstrap";
import {
  ArrowDownRight,
  ArrowUpRight,
  QuestionLg,
  CheckLg,
  BoxArrowUpRight,
} from "react-bootstrap-icons";

import { Doughnut, Pie } from "react-chartjs-2";
import { Chart, ArcElement, Tooltip, Title, Legend } from "chart.js";

Chart.register(ArcElement, Tooltip, Title, Legend);

const SpeciesList = () => {
  const { state } = useLocation();
  const commonThreat = state.commonThreat;
  const speciesList = state.speciesList;
  const counter = state.counter;

  const labels = new Array();
  const d = new Array();
  for (let key in counter) {
    labels.push(key);
    d.push(counter[key]);
  }

  // console.log(data);

  const centerText = {
    textAlign: "center",
  };

  const data = {
    labels: labels,
    datasets: [
      {
        data: d,
        backgroundColor: [
          "#b56576",
          "#e56b6f",
          "#cdb4db",
          "#ffc8dd",
          "#ffafcc",
          "#bde0fe",
          "#a2d2ff",
          "#c7f9cc",
          "#80ed99",
          "#57cc99",
          "#38a3a5",
          "#22577a",
        ],
        hoverOffset: 4,
      },
    ],
    options: {
      legend: {
        display: "true",
        position: "top",
      },
    },
  };

  return (
    <>
      {speciesList.length !== 0 ? (
        <>
          <Container style={{ maxWidth: "1000px" }}>
            <br />
            <h2 style={centerText}>Most Common Threat: {commonThreat}</h2>
            <br />
            <Doughnut data={data} />
          </Container>
          <br />
          <Container>
            <h2 style={centerText}>Species List</h2>
            <br />
            <ListGroup>
              {speciesList.map((item) => {
                let color = "gray";
                let arrowIcon = <QuestionLg />;

                if (item.population === "Decreasing") {
                  color = "red";
                  arrowIcon = <ArrowDownRight />;
                } else if (item.population === "Increasing") {
                  color = "green";
                  arrowIcon = <ArrowUpRight />;
                } else if (item.population === "Stable") {
                  color = "black";
                  arrowIcon = <CheckLg />;
                }

                const style = {
                  color: color,
                };

                const externalLinkStyle = {
                  color: "gray",
                  cursor: "pointer",
                };

                return (
                  <ListGroup.Item>
                    <Container>
                      <Row>
                        <Col>
                          <h3>
                            <i>{item.name}</i>{" "}
                            <BoxArrowUpRight
                              style={externalLinkStyle}
                              onClick={() => {
                                window.open(item.url);
                              }}
                            />
                          </h3>
                          <h5>
                            Population Trend:{" "}
                            <span style={style}>
                              {item.population}
                              {arrowIcon}
                            </span>
                          </h5>
                        </Col>
                        <Col xs={3} style={centerText}>
                          {item.imageURL && <img src={item.imageURL}></img>}
                          {!item.imageURL && "No image"}
                        </Col>
                      </Row>
                    </Container>
                  </ListGroup.Item>
                );
              })}
            </ListGroup>
          </Container>{" "}
        </>
      ) : (
        <>
          <br />
          <h1 style={centerText}>No species found</h1>
        </>
      )}
    </>
  );
};

export default SpeciesList;
