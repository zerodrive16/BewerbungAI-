import React, {useState} from 'react';
import "./style/Navbar.css";
import { Button } from './Button';
import { Link } from 'react-router-dom';
import { kc } from '../App';
import axios from 'axios';

function Navbar(){
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
  const handleLogout = () => {
      console.log("Hello World")
    fetchCSRFToken();
      kc.logout({
        redirectUri: "https://127.0.0.1:8000/"
      });
      localStorage.removeItem('keycloakToken');
      sessionStorage.clear();
      window.location.reload();
  };
    return(
    <nav className="navbar navbar-expand-lg col-12">
       <h1 className="navbar-brand col-2">BewerbungAI</h1>
       <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
       </button>
       <div className="collapse navbar-collapse justify-content-end col-8" id="navbarNavDropdown">
           <ul className="header-nav navbar-nav">
              <li className="nav-item">
                     <Link to="/home" className="nav-link">
                 BewerbungAI</Link>
              </li>
              <li className="nav-item">
                 <Link to="/resume" className="nav-link">
                 Personal Information</Link>
              </li>
              <li className="nav-item">
                 <Link to="/history" className="nav-link">
                 History</Link>
              </li>
              <li className="nav-item">
                 <a href="http://localhost:8080/realms/myrealm/account/" className="nav-link">
                 Profile
                 </a>
              </li>
              <li className="nav-item">
                 <button onClick={handleLogout} className="nav-link">
                 Sign Out
                 </button>
              </li>
           </ul>
       </div>
    </nav>

    );
}

export default Navbar;

