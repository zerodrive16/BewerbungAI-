import React from 'react';
import "./style/Footer.css";
import "./style/Navbar.css";
import { Link } from 'react-router-dom';


function Footer(){
    return(
        <div className="footer">
            <ul className="footer-nav navbar-nav">
                <li className="nav-item">
                     <Link to="/" className="nav-link">BewerbungAI</Link>
                </li>
                <li className="nav-item"> | </li>
                <li className="nav-item">
                     <Link to="/aboutUs" className="nav-link"> About us</Link>
                </li>
            </ul>
        </div>
    )
};

export default Footer;