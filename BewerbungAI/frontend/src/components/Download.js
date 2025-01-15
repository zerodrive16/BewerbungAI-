import React, { useState, useEffect } from 'react';
import Button from "./Button.js";
import axios from 'axios';

function Download() {
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');
  const getCSRFToken = () => {
      const csrfToken = sessionStorage.getItem('csrfToken');
      if (csrfToken) {
        return csrfToken;
      }
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrfToken') {
          return value;
        }
      }
      return null;
  };
/*
  const fetchScriptOutput = () => {
       console.log("thinking..");
    axios.get('http://127.0.0.1:8000/download/api')
      .then(response => {
        console.log(response.data.output)
        setOutput(response.data.output);
      })
      .catch(err => {
        console.error('Error fetching data:', err);
        setError('Failed to fetch script output');
      });
        console.log(output);
  };
  */
  const executeScript = async (e) => {
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
      if (response.ok) {
        const data = await response.json();
        console.log(data);
      } else {
        const errorData = await response.json();
        console.log(`Error: ${errorData.error}`);
      }
    } catch (error) {
      console.log("An error occurred: " + error.message);
    }
  };

  useEffect(() => {
    executeScript();
    console.log("script executed")
  }, []);

  return (
  <>
    <a href="http://127.0.0.1:8000/static/text.txt" download="text.txt">
      <Button style={{border: "1px solid rgb(82, 82, 82)"}}>Download File</Button>
    </a>
   </>
  );
}

export default Download;