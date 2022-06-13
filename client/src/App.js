import Nav from "./components/Nav";
import Landing from "./components/Landing";
import SpeciesList from "./components/SpeciesList";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "./App.css";

function App() {
  return (
    <Router>
      <Nav />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/list" element={<SpeciesList />} />
      </Routes>
    </Router>
  );
}

export default App;
