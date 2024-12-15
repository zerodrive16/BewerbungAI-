import React from 'react';
import Navbar from "./Navbar.js";
import Button from "./Button.js";
import Footer from "./Footer.js";


function Application(){
  return (
    <div>
      <div className="header d-flex flex-column justify-content-center">
        <Navbar />
      </div>
        <Footer />
    </div>
  );
}

export default Application;