import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from "./components/Home.js";
import AboutUs from "./components/AboutUs.js";
import Resume from "./components/Resume.js";
import Application from "./components/Application.js";

export default function App(){
  return (
    <Router>
      <div className="content">
        <Routes>
          <Route path="/" element={<Home />}  />
          <Route path="/resume" element={<Resume />}  />
          <Route path="/application" element={<Application />} />
          <Route path="/aboutUs" element={<AboutUs />} />
        </Routes>
      </div>
    </Router>
  );
}
