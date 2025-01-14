import React from 'react';
import Navbar from "./Navbar.js";
import Button from "./Button.js";
import Footer from "./Footer.js";


function AboutUs(){
  return (
    <div className="box">
      <div className="header d-flex flex-column justify-content-center">
        <Navbar />
      </div>
      <div className="main"></div>
      <Footer />
    </div>
  );
}

export default AboutUs;