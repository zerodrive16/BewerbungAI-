import React, { useState, useEffect,  } from 'react';
import Navbar from "./Navbar.js";
import Button from "./Button.js";
import InputForm from "./InputForm.js";
import Footer from "./Footer.js";
import "./Application.css";
import { useNavigate } from "react-router";


function Application(){
  const navigate = useNavigate();
  const [inputValue, setInputValue] = useState({
      job: ""
    });

  // Function to extract CSRF token from cookies
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

  const handleChange = (e) => {
    const { name, value } = e.target;
    setInputValue((prevState) => ({ ...prevState, [name]: value }));
  };
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const csrfToken = getCSRFToken();
      if (!csrfToken) {
        throw new Error('CSRF token is missing. Make sure the backend sets it.');
      }
      const response = await fetch('application/api', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ value: inputValue })
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      navigate('/result');
      console.log(data); // Process the response data
    } catch (err) {
      console.error('Error:', err);
    }
  };
  return (
  <div className="body">
    <div>
      <Navbar />
      <h3 className="title">Job description </h3>
      <form onSubmit={handleSubmit} className="job_info">
        <div className="job_info_input">
          <textarea className="job_info_content col-7" label="Job descripbtion" type="text" name="job" value={inputValue.job} onChange={handleChange} placeholder="Job descripbtion" required></textarea>
        </div>
        <div className="job_info_button">
          <Button colSize="col" colNumber="2" type="submit" style={{ border: "1px solid #525252", margin: "2rem" }}>
            Submit
          </Button>
        </div>
      </form>
    </div>
      <Footer />
    </div>
  );
}

export default Application;