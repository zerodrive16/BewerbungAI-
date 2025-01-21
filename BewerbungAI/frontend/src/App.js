import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Home from "./components/Home.js";
import AboutUs from "./components/AboutUs.js";
import Resume from "./components/Resume.js";
import Application from "./components/Application.js";
import Output from "./components/Output.js";
import Result from "./components/Result.js";
import History from "./components/History.js";
import HistoryDetails from "./components/HistoryDetails.js";
import "./App.css";
import { exportUsersToDjango } from './api';
//import "primereact/resources/themes/lara-light-indigo/theme.css";
//import "primereact/resources/primereact.min.css";
//import "primeflex/primeflex.css";
import { httpClient } from './components/HttpClient';
import Keycloak from 'keycloak-js';
import useCSRFToken from './hook/useCSRFToken'; // Import the custom hook
import axios from 'axios';

const initOptions = {
  url: 'http://localhost:8080/',
  realm: 'myrealm',
  clientId: 'myclient',
};


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
const kc = new Keycloak(initOptions);
// App Component
export default function App() {
  const { csrfToken, error: csrfError } = useCSRFToken(); // Use the custom hook
  const [keycloakInitialized, setKeycloakInitialized] = useState(false);

  useEffect(() => {
    kc.init({
      onLoad: 'login-required',
      checkLoginIframe: false,
      pkceMethod: 'S256',
      prompt: 'login', // Force login on each session start
    })
      .then((auth) => {
        if (!auth) {
          console.warn('Not authenticated. Reloading...');
          window.location.reload();
        } else {
          console.info('Authenticated');

          // Call the export function to sync users
          exportUsersToDjango(kc.token)
            .then((data) => {
              if (data.status === 'success') {
                console.log('Users exported successfully:', data.message);
              } else {
                console.error('Error exporting users:', data.message);
              }
            })
            .catch((error) => {
              console.error('Failed to export users:', error);
            });

          kc.onTokenExpired = () => {
            console.log('Token expired. Refreshing...');
            kc.updateToken(30).catch(() => {
              console.error('Failed to refresh token. Logging out...');
              kc.logout();
            });
          };
          setKeycloakInitialized(true);

        }
      })
      .catch((error) => {
        console.error('Keycloak initialization failed:', error);
      });
  }, []);

  if (!keycloakInitialized) {
    return <div>Loading...</div>;
  }

  if (csrfError) {
    return <div>Error: Unable to fetch CSRF token. Please try again later.</div>;
  }

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
          <Route path="/" element={<Navigate to="/home" />} /> {/* Redirect to Home */}
          <Route path="/result" element={<Result />} />
          <Route path="/history" element={<History />} />
          <Route path="/historyDetails/:id" element={<HistoryDetails />} />
        </Routes>
      </div>
    </Router>
  );
}
