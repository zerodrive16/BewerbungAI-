import React from 'react';
import Navbar from "./Navbar.js";
import Button from "./Button.js";
import "./Home.css";
import { Link } from 'react-router-dom';


function Home(){
    const buttonStyle = {
        backgroundColor: 'rgb(255, 255, 255, 0.8)',
        color: '#525252',
        padding: '10px 20px',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
        marginBottom: '5%',
    };
    const items = [
        {
            title: "1. Fill out the form.",
            img: "/frontend/build/static/img/form.png",
        }
    ];
    return (
        <div>
            <div className="home-header d-flex flex-column justify-content-center">
                <Navbar/>
                <div class="content-header">
                    <p className="col-4 d-flex text-align-center">Create your perfect resume in just a few minutes!
                       Simply sign up, enter your details, and receive
                       a professional document – fast, personalized,
                       and free.
                    </p>
                    <Button style = {buttonStyle} colSize="col" colNumber="1">
                     <Link to="/resume" className="nav-link">Get started</Link>
                    </Button>
                </div>
            </div>
            <div>
                <h2 className="title_body">So erstellst du mit Name ein Anschreiben</h2>
                <ul className="list_steps">
                    {items.map(item => (
                        <li className="item">
                            <h2>{item.title}</h2>
                            <img src={item.img} alt={item.title}/>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default Home;