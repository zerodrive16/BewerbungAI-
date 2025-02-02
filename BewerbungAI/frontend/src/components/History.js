import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Link, useNavigate } from "react-router-dom";
import Navbar from "./Navbar.js";
import Footer from "./Footer.js";
import Button from "./Button.js";
import "./style/History.css";
import { useUser } from './UserContext';

function History(){
  const [jsonData, setJsonData] = useState([]);
  const [previewText, setPreviewText] = useState("");
  const navigate = useNavigate();
  const user = useUser(null);

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
      .then((response) => {
        if (response.ok && response.headers.get("Content-Type").includes("application/json")) {
          return response.json();
        }
        throw new Error("Not a JSON response");
      })
      .then((data) => {
        if(!data){
            data = "No application letter generated!";
        }
        console.log(data);
        let result = []
        if(user.email){
          for (let i = 0; i < Object.keys(data).length; i++) {
            console.log("email, user.email, boolean",data[i].email, user.email, data[i].email === user.email);
            if (data[i].email === user.email) {
              result.push(data[i]);
            }
          }
        }
        console.log("result:", result);
        if(result.length === 0){
          result = "No application letter generated!";
        }
        setJsonData(result);
      })
       .catch((error) => {
        console.error("Error fetching data:", error);
      })
  }, []);



  const handleHistoryItemClick = (id) => {
    navigate(`/historyDetails/${id}`);
  };

  return (
    <div className="download box">
      <Navbar />
      <div className="main result col-12">
        <h3 className="title">History</h3>
        <div class="history_list d-flex flex-column align-items-center col-12 mb-3">
        {Array.isArray(jsonData) ? (
          jsonData.map((item) => (
            <li className="history_items col-7" key={item.id} onClick={() => handleHistoryItemClick(item.id)}>
              {item.date}:  {item.companyName} - {item.jobFieldName}
            </li>
          ))
        ) : (
        <>
          <p className="no_history_item history_items col-7">{jsonData}</p>
          <Button className="col-3" type="button">
            <Link to="/resume" className="header-link no-decoration">Get started</Link>
          </Button>
        </>
        )}
      </div>
      </div>
      <Footer />
    </div>
  );
}

export default History;