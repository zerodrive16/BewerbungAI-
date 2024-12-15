import React from 'react';
import Navbar from "./Navbar.js";
import Button from "./Button.js";
import Footer from "./Footer.js";
import "./Resume.css"


function Resume(){
  return (
    <div>
      <div className="resume-header d-flex flex-column justify-content-center">
        <Navbar />
      </div>
        <Footer />
    </div>
  );
}

export default Resume;