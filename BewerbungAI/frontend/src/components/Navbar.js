import React, {useState} from 'react';
import "./Navbar.css";
import { Button } from './Button';
import { Link } from 'react-router-dom';

function Navbar(){
    return(
    <nav className="navbar navbar-expand-lg d-flex justify-content-between ">
       <h1 className="navbar-brand d-flex align-items-center col-2">BewerbungAI</h1>
       <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
       </button>
       <div class="collapse navbar-collapse justify-content-end col-8" id="navbarNavDropdown">
           <ul className="navbar-nav">
              <li className="nav-item">
                 <Link to="/" className="nav-link">
                 BewerbungAI</Link>
              </li>
              <li className="nav-item">
                 <Link to="/resume" className="nav-link">
                 Resume</Link>
              </li>
              <li className="nav-item">
                 <Link to="/application" className="nav-link">
                 Application Letter</Link>
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

