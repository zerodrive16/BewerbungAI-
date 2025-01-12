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
      name: "",
      surname: "",
      birthday: "",
      birthplace: "",
      nationality: "",
      address: "",
      phone: "",
      email: "",
      experience: "",
      education: "",
      skills: "",
      languages: "",
      interests: "",
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
      <h3 className="pers_info_title">Personal information</h3>
      <form onSubmit={handleSubmit} className="pers_info">
        <div className="pers_info_input">
          <div className="pers_info_col col-5">
            <InputForm
              label="Name"
              type="text"
              name="name"
              value={inputValue.name}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Surname"
              type="text"
              name="surname"
              value={inputValue.surname}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Date of birth"
              type="text"
              name="birthday"
              value={inputValue.birthday}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Place of birth"
              type="text"
              name="birthplace"
              value={inputValue.birthplace}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Nationality"
              type="text"
              name="nationality"
              value={inputValue.nationality}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Address"
              type="text"
              name="address"
              value={inputValue.address}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Phone"
              type="text"
              name="phone"
              value={inputValue.phone}
              onChange={handleChange}
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
              label="Work experience"
              type="text"
              name="experience"
              value={inputValue.experience}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Education"
              type="text"
              name="education"
              value={inputValue.education}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Skills"
              type="text"
              name="skills"
              value={inputValue.skills}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Languages"
              type="text"
              name="languages"
              value={inputValue.languages}
              onChange={handleChange}
              required
            />
            <InputForm
              label="Interests"
              type="text"
              name="interests"
              value={inputValue.interests}
              onChange={handleChange}
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
