import React from 'react';
import Navbar from "./Navbar.js";
import Button from "./Button.js";
import InputForm from "./InputForm.js";
import Footer from "./Footer.js";
import ApplicationForm from "./ApplicationForm.js";


function Application(){
  return (
    <div>
      <div className="header d-flex flex-column justify-content-center">
        <Navbar />
      </div>
        <ApplicationForm />
        <Footer />
    </div>
  );
}

export default Application;