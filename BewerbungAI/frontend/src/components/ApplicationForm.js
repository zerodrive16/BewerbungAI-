import React, { useState } from 'react';
import axios from 'axios';

function ApplicationForm() {
  // State for form inputs
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  });

  // State for success or error messages
  const [responseMessage, setResponseMessage] = useState('');

    // Handle form input changes
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };
    const getCSRFTokenFromCookie = () => {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
          console.log(value);
          return value;
        }
      }
      return null;
    };
  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent default form behavior
    const csrfToken = getCSRFTokenFromCookie();
      if (!csrfToken) {
        throw new Error('CSRF token is missing. Make sure the backend sets it.');
      }
    axios.post('http://127.0.0.1:8000/application/api', formData, {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken, // Include the CSRF token
        },
        })
      .then((response) => {
        console.log('Response:', response.data);
        setResponseMessage('Form submitted successfully!');
      })
      .catch((error) => {
        console.error('Error posting form data:', error);
        setResponseMessage('Failed to submit form.');
      });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Message:</label>
          <textarea
            name="message"
            value={formData.message}
            onChange={handleChange}
            required
          ></textarea>
        </div>
        <button type="submit">Submit</button>
      </form>
      {responseMessage && <p>{responseMessage}</p>}
    </div>
  );
}

export default ApplicationForm;
