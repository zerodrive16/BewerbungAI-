import React, { useState, useEffect } from 'react';
import axios from 'axios';
import InputForm from "./InputForm.js";
import Navbar from "./Navbar.js";
import Footer from "./Footer.js";
import Button from "./Button.js";
import "./style/Resume.css";
import { useNavigate } from "react-router";

axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.withCredentials = true;

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

  const [errors, setErrors] = useState({});

  useEffect(() => {
    const today = new Date();
    const day = String(today.getDate()).padStart(2, '0');  // Ensure two digits for day
    const month = String(today.getMonth() + 1).padStart(2, '0');  // Ensure two digits for month (months are 0-indexed)
    const year = today.getFullYear();
    const formattedDate = `${day}.${month}.${year}`;  // Format: DD.MM.YYYY
    setInputValue(prev => ({ ...prev, date: formattedDate }));
}, []);

  const fields = [
    { id: 1, label: "First name", name: "first_name", required: true, maxLength: 20 },
    { id: 2, label: "Last name", name: "last_name", required: true, maxLength: 20 },
    { id: 3, label: "Date of birth (DD.MM.YYYY)", name: "birthday", required: true, maxLength: 10 },
    { id: 4, label: "Address", name: "address", required: true, maxLength: 50 },
    { id: 5, label: "City", name: "city", required: true, maxLength: 50 },
    { id: 6, label: "Zipcode", name: "zipcode", required: true, maxLength: 10 },
    { id: 7, label: "Phone", name: "phone", required: true, maxLength: 17 },
    { id: 8, label: "E-Mail", name: "email", required: false, maxLength: 100 },
  ];
  const textarea = [
    { id: 10, label: "Work experience", name: "experience", required: true, maxLength: 200 },
    { id: 11, label: "Education", name: "education", required: true, maxLength: 200 },
    { id: 12, label: "Skills", name: "skills", required: true, maxLength: 200 },
    { id: 13, label: "Interests", name: "interests", required: true, maxLength: 200 }
  ];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setInputValue(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newErrors = {};
    fields.forEach(field => {
      if (field.required && !inputValue[field.name]) {
        newErrors[field.name] = `${field.label} is required.`;
      }
    });

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    try {
      const response = await axios.post('resume/api', { value: inputValue });
      navigate('/application');
    } catch (err) {
      console.error('Error:', err);
    }
  };

  return (
    <div className="box">
      <Navbar />
      <div className="main">
        <h3 className="title">Personal information</h3>
        <form onSubmit={handleSubmit} className="pers_info">
          <div className="pers_info_input">
            <div className="pers_info_field">
              <input
                className="input"
                label="Date"
                type="text"
                name="date"
                value={inputValue.date}
                required
                onChange={handleChange}
              />
              {fields.map(field => (
                <div key={field.id} className="input-form">
                  <input
                    className="input"
                    label={field.label}
                    type="text"
                    name={field.name}
                    placeholder={field.label}
                    maxLength={field.maxLength}
                    value={inputValue[field.name]}
                    required={field.required}
                    onChange={handleChange}
                  />
                  {errors[field.name] && <span className="error">{errors[field.name]}</span>}
                </div>
              ))}
            </div>
            <div className="pers_info_textarea">
              {textarea.map(textarea => (
                <div key={textarea.id} className="input-form">
                  <textarea
                    className="per_info_content"
                    label={textarea.label}
                    type="text"
                    name={textarea.name}
                    placeholder={textarea.label}
                    maxLength={textarea.maxLength}
                    value={inputValue[textarea.name]}
                    required={textarea.required}
                    onChange={handleChange}
                  />
                  {errors[textarea.name] && <span className="error">{errors[textarea.name]}</span>}
                </div>
              ))}
            </div>
          </div>
          <div className="pers_info_button">
            <Button colSize="col" colNumber="2" type="submit" style={{ border: "1px solid #525252" }}>
              Submit
            </Button>
          </div>
        </form>
      </div>
      <Footer />
    </div>
  );
}

export default Resume;
