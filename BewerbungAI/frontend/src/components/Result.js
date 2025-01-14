import React, { useState, useEffect,  } from 'react';
import Navbar from "./Navbar.js";
import Footer from "./Footer.js";
import Download from "./Download.js";
import "./style/Result.css";

function Result(){
  const [fileContent, setFileContent] = useState("");
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
  const fetchFileContent = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/static/text.txt");
      if (!response.ok) {
        throw new Error("Failed to fetch the file.");
      }
      const text = await response.text();
      console.log(text)
      setFileContent(text); // Store the content in state
    } catch (error) {
      console.error("Error fetching file:", error);
      setFileContent("Error loading content.");
    }
  };
  useEffect(() => {
    fetchFileContent(); // Fetch file content when the component mounts
  }, []);

  return (
    <div className="download box">
      <Navbar />
      <div className="main result">
        <h3 className="title">Application letter</h3>
        <div className="download_preview">
          <pre>{fileContent}</pre>
        </div>
        <div className="download_button">
          <Download/>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Result;