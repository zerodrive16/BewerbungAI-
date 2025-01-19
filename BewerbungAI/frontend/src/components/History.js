import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Link, useNavigate } from "react-router-dom";
import Navbar from "./Navbar.js";
import Footer from "./Footer.js";
import Button from "./Button.js";
import "./style/History.css";

function History(){
  const [jsonData, setJsonData] = useState([]);
  const [previewText, setPreviewText] = useState("");
  const navigate = useNavigate();

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
      .then((data) => setJsonData(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  const handleHistoryItemClick = (id) => {
    navigate(`/historyDetails/${id}`);
  };

  return (
    <div className="download box">
      <Navbar />
      <div className="main result">
        <h3 className="title">History</h3>
        <ul>
        {jsonData.map((item) => (
          <li className="history_items" key={item.id} onClick={() => handleHistoryItemClick(item.id)}>
            {item.date}:  {item.companyName} - {item.jobFieldName}
          </li>
        ))}
      </ul>
      </div>
      <Footer />
    </div>
  );
}

export default History;