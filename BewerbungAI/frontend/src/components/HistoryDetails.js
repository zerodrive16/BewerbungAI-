import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Navbar from "./Navbar.js";
import Footer from "./Footer.js";
import Button from "./Button.js";
import { useParams } from 'react-router-dom';

function HistoryDetails({ id, date, companyName, jobFieldName }) {
  const { id: paramsId } = useParams();
  const [jsonData, setJsonData] = useState([]);

  console.log(paramsId)
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

  useEffect(() => {
    fetch("/dataset/api")
      .then((response) => response.json())
      .then((data) => {
        const needed_item = data[paramsId -1];
        setJsonData(needed_item);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);
  console.log(jsonData);
  return (
    <div className="box">
      <Navbar />
      <div className="main history_details d-flex flex-column align-items-center p-4">
        <h2 className="title">History Item Details</h2>
        <div className="history_text download_preview">Date: {jsonData.jobApplicationContent}</div>
      </div>
      <Footer />
    </div>
  );
}

export default HistoryDetails;
