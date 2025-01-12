import React, { useState, useEffect,  } from 'react';
import Navbar from "./Navbar.js";
import Footer from "./Footer.js";
import Download from "./Download.js";

function Result(){
  const getCSRFToken = () => {
      // First, try to get the token from sessionStorage
      const csrfToken = sessionStorage.getItem('csrfToken');
      if (csrfToken) {
        return csrfToken;
      }
      // If not found in sessionStorage, try to extract from cookies
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrfToken') {
          return value;
        }
      }
      return null;  // Return null if no CSRF token is found
  };


  return (
    <div>
      <Navbar />
      <h3 className="title">Application letter</h3>
      <Download/>
      <Footer />
    </div>
  );
}

export default Result;