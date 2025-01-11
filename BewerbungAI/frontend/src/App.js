import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Home from "./components/Home.js";
import AboutUs from "./components/AboutUs.js";
import Resume from "./components/Resume.js";
import Application from "./components/Application.js";
import Output from "./components/Output.js";
import "./App.css";
import "primereact/resources/themes/lara-light-indigo/theme.css";
import "primereact/resources/primereact.min.css";
import "primeflex/primeflex.css";
import { httpClient } from './components/HttpClient';
import Keycloak from 'keycloak-js';
import useCSRFToken from './hook/useCSRFToken'; // Import the custom hook

const initOptions = {
  url: 'http://localhost:8080/',
  realm: 'myrealm',
  clientId: 'myclient',
};

const kc = new Keycloak(initOptions);

function App() {
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
          httpClient.defaults.headers.common['Authorization'] = `Bearer ${kc.token}`;
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
        </Routes>
      </div>
    </Router>
  );
}

export default App;
