import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from "./components/Home.js";
import AboutUs from "./components/AboutUs.js";
import Resume from "./components/Resume.js";
import Application from "./components/Application.js";
import Output from "./components/Output.js";
import Result from "./components/Result.js";
import History from "./components/History.js";
import HistoryDetails from "./components/HistoryDetails.js";
import "./App.css";

import axios from 'axios';

// Fetch CSRF token when the app starts
const fetchCSRFToken = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/get-csrf-token', {
      withCredentials: true,  // Make sure credentials are included (cookies)
    });
    const csrfToken = response.data.csrfToken;

    // Store the CSRF token globally, e.g., in sessionStorage
    sessionStorage.setItem('csrfToken', csrfToken);

    // Optionally, you can set it as a global Axios header here
    axios.defaults.headers['X-CSRFToken'] = csrfToken;
  } catch (error) {
    console.error('Error fetching CSRF token:', error);
  }
};

// Call this function on page load or app initialization
fetchCSRFToken();

// App Component
export default function App() {
  // Render the application once authenticated
  return (
    <Router>
      <div className="content">
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/resume" element={<Resume />} />
          <Route path="/application" element={<Application />} />
          <Route path="/aboutUs" element={<AboutUs />} />
          <Route path="/output" element={<Output />} />
          <Route path="/result" element={<Result />} />
          <Route path="/history" element={<History />} />
          <Route path="/historyDetails/:id" element={<HistoryDetails />} />
        </Routes>
      </div>
    </Router>
  );
}
