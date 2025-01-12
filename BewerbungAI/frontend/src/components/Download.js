import React, { useState } from 'react';
import axios from 'axios';


function Download() {

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
  const executeScript = async (e) => {
    e.preventDefault();
    try {
      const csrfToken = getCSRFToken();
      if (!csrfToken) {
        throw new Error('CSRF token is missing. Make sure the backend sets it.');
      }
      const response = await fetch("download/api", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': csrfToken
        },
      });
      console.log("waiting")
      if (response.ok) {
        console.log(response)
        const data = await response.json();
        alert(data.message);
      } else {
        console.log(response)
        const errorData = await response.json();
        alert(`Error: ${errorData.error}`);
      }
    } catch (error) {
      alert("An error occurred: " + error.message);
    }
  };


  return (
  <>
   <button onClick={executeScript}>
      Run Python Script
    </button>
    <a href=" http://127.0.0.1:8000/static/text.txt" download="text.txt">
      <button>Download File</button>
    </a>
   </>
  );
}

export default Download;