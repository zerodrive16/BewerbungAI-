import React, { useState, useEffect,  } from 'react';
import Navbar from "./Navbar.js";
import Footer from "./Footer.js";
import Button from "./Button.js";
import "./style/Result.css";

function Result(){
  const [jsonData, setJsonData] = useState([]);
  const [lastEntry, setLastEntry] = useState([]);
  const [previewText, setPreviewText] = useState("");

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
    // Function to format text
  const formatText = (inputText) => {
    const maxLineLength = 90;
    const minLineLength = 70;

    let lines = [];
    let currentLine = "";
    inputText.split(" ").forEach((word) => {
      if ((currentLine + word).length > maxLineLength) {
        lines.push(currentLine.trim());
        currentLine = word + " ";
      } else if ((currentLine + word).length >= minLineLength && word.endsWith(".")) {
        currentLine += word + " ";
        lines.push(currentLine.trim());
        currentLine = "";
      } else {
        currentLine += word + " ";
      }
    });
    if (currentLine.trim()) {
      lines.push(currentLine.trim());
    }
    return lines.join("\n");
  };

  useEffect(() => {
    fetch("/dataset/api")
      .then((response) => response.json())
      .then((data) => {
        setJsonData(data);
        if (data && data.length > 0) {
          const lastItem = data[data.length - 1];
          setLastEntry(lastItem);
          console.log(lastItem);
          transformDataToText(lastItem);
          console.log("Last entry from data:", lastItem);
        } else {
          setLastEntry(null);
        }
      });
  }, []);
  const transformDataToText = (data) => {
    const appl_letter = formatText(data.jobApplicationContent);
    const textContent = `${appl_letter}`;
    setPreviewText(textContent);
  };
  const downloadTextFile = () => {
    const blob = new Blob([previewText], { type: "text/plain" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "dataset.txt";
    link.click();
  };

  return (
    <div className="download box">
      <Navbar />
      <div className="main result col-12">
        <h3 className="title">Application letter</h3>
        <div className="download_preview col-10 col-md-12">
          <pre>{previewText}</pre>
        </div>
        <div className="download_button">
           <Button onClick={downloadTextFile}>Download</Button>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Result;