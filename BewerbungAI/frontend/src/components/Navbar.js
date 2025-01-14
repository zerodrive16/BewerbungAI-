import React, {useState} from 'react';
import "./style/Navbar.css";
import { Button } from './Button';
import { Link } from 'react-router-dom';

function Navbar(){
    return(
    <nav className="navbar navbar-expand-lg col-12">
       <h1 className="navbar-brand col-2">BewerbungAI</h1>
       <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
       </button>
       <div className="collapse navbar-collapse justify-content-end col-8" id="navbarNavDropdown">
           <ul className="header-nav navbar-nav">
              <li className="nav-item">
                     <Link to="/home" className="nav-link">
                 BewerbungAI</Link>
              </li>
              <li className="nav-item">
                 <Link to="/resume" className="nav-link">
                 Personal Information</Link>
              </li>
              <li className="nav-item">
                 <Link to="/aboutUs" className="nav-link">
                 About us</Link>
              </li>
           </ul>
       </div>
    </nav>

    );
}

export default Navbar;

