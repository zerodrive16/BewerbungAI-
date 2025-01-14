import React, { useState, useEffect,  } from 'react';
import Navbar from "./Navbar.js";
import Button from "./Button.js";
import InputForm from "./InputForm.js";
import Footer from "./Footer.js";
import "./style/Application.css";
import { useNavigate } from "react-router";


function Application(){
  const navigate = useNavigate();
  const [inputValue, setInputValue] = useState({
      job: ""
    });
  const job_content = [
    {
      id: 1,
      label: "Manager name",
      type: "text",
      name: "manager_name",
      value: inputValue.manager_name,
      pattern: ".*",
      maxLength: 30,
      required: true
    },
    {
      id: 2,
      label: "Company name",
      type: "text",
      name: "company_name",
      value: inputValue.company_name,
      pattern: ".*",
      maxLength: 25,
      required: true
    },
    {
      id: 3,
      label: "Company address",
      type: "text",
      name: "company_address",
      value: inputValue.company_address,
      pattern: ".*",
      maxLength: 50,
      required: true
    },
    {
      id: 4,
      label: "Company city",
      type: "text",
      name: "company_city",
      value: inputValue.company_city,
      pattern: ".*",
      maxLength: 50,
      required: true
    },
    {
      id: 5,
      label: "Company zip code",
      type: "text",
      name: "company_zip_code",
      value: inputValue.company_zip_code,
      pattern: ".*",
      maxLength: 10,
      required: true
    },
    {
      id: 6,
      label: "Job field name",
      type: "text",
      name: "job_field_name",
      value: inputValue.job_field_name,
      pattern: ".*",
      maxLength: 50,
      required: true
    }
  ]
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
  <div className="box">
    <Navbar />
    <div className="main">
      <h3 className="title">Job description </h3>
      <form onSubmit={handleSubmit} className="job_info">
        <div className="job_info_first">
        {job_content.map((job_content) => (
          <div key={job_content.id} className="input-form ">
            <input className="input"
              label={job_content.label}
              type={job_content.type}
              name={job_content.name}
              placeholder={job_content.label}
              pattern={job_content.pattern}
              maxLength={job_content.maxLength}
              value={inputValue[job_content.name]}
              required={job_content.required}
              onChange={handleChange}
            />
          </div>
        ))}
        </div>
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