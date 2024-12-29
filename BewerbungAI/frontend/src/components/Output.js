import React from 'react';
import Navbar from "./Navbar.js";
import Button from "./Button.js";
import Footer from "./Footer.js";
import { useState, useEffect } from 'react';
import axios from 'axios';


function Output(){
 const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const fetchScriptOutput = () => {
       console.log("thinking..");
    axios.get('http://127.0.0.1:8000/backend')
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

  return (
    <div>
      <button onClick={fetchScriptOutput}>Run Script</button>
      <p className="api">Output: {output || 'No output yet'}</p>
      <p className="api">Error: {error || 'No errors'}</p>
    </div>
  );
}

export default Output;