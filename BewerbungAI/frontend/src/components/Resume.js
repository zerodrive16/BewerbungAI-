import React, { useState, useEffect,  } from 'react';
import axios from 'axios';
import InputForm from "./InputForm.js";
import Navbar from "./Navbar.js";
import Footer from "./Footer.js";
import Button from "./Button.js";
import "./Resume.css";
import { useNavigate } from "react-router";

axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.withCredentials = true; // Ensure credentials (cookies) are sent

function Resume() {
  const navigate = useNavigate();
  const [inputValue, setInputValue] = useState({
      first_name: "",
      last_name: "",
      birthday: "",
      address: "",
      city: "",
      zipcode: "",
      phone: "",
      email: "",
      date: "",
      experience: "",
      education: "",
      skills: "",
      interests: ""
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
      const response = await fetch('resume/api', {
        method: 'POST',
        headers: {
          'Content-Type': 'resume/json',
          'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ value: inputValue })
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      navigate('/application');
      console.log(data); // Process the response data
    } catch (err) {
      console.error('Error:', err);
    }
  };
  return (
    <div>
      <Navbar />
      <h3 className="title">Personal information</h3>
      <form onSubmit={handleSubmit} className="pers_info">
        <div className="pers_info_input">
          <div className="pers_info_col col-5">
            <InputForm
              label="First name"
              type="text"
              name="first_name"
              value={inputValue.first_name}
              onChange={handleChange}
              maxLength="20"
              required
            />
            <InputForm
              label="Last name"
              type="text"
              name="last_name"
              value={inputValue.last_name}
              onChange={handleChange}
              maxLength="20"
              required
            />
            <InputForm
              label="Date of birth"
              type="text"
              name="birthday"
              value={inputValue.birthday}
              onChange={handleChange}
              errorMessage="DateTime must be in the format DD/MM/YYYY"
              required
            />
            <InputForm
              label="Address"
              type="text"
              name="address"
              value={inputValue.address}
              onChange={handleChange}
              maxLength="50"
              required
            />
            <InputForm
              label="City"
              type="text"
              name="city"
              value={inputValue.city}
              onChange={handleChange}
              maxLength="50"
              required
            />
            <InputForm
              label="Zipcode"
              type="text"
              name="zipcode"
              value={inputValue.zipcode}
              onChange={handleChange}
              maxLength="17"
              required
            />
            <InputForm
              label="Phone"
              type="text"
              name="phone"
              value={inputValue.phone}
              onChange={handleChange}
              maxLength="17"
              required
            />
            <InputForm
              label="E-Mail"
              type="email"
              name="email"
              value={inputValue.email}
              onChange={handleChange}
            />
          </div>
          <div className="pers_info_col col-5">
            <InputForm
              label="Date"
              type="text"
              name="date"
              value={inputValue.date}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Work experience"
              type="text"
              name="experience"
              value={inputValue.experience}
              onChange={handleChange}
              maxLength="200"
              required
            />
            <InputForm
              label="Education"
              type="text"
              name="education"
              value={inputValue.education}
              onChange={handleChange}
              maxLength="200"
              required
            />
            <InputForm
              label="Skills"
              type="text"
              name="skills"
              value={inputValue.skills}
              onChange={handleChange}
              maxLength="200"
              required
            />
            <InputForm
              label="Interests"
              type="text"
              name="interests"
              value={inputValue.interests}
              onChange={handleChange}
              maxLength="200"
              required
            />
          </div>
        </div>
        <div className="pers_info_button">
          <Button colSize="col" colNumber="2" type="submit" style={{ border: "1px solid #525252" }}>
            Submit
          </Button>
        </div>
      </form>
      <Footer />
    </div>
  );
}

export default Resume;
