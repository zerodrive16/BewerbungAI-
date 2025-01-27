import React from 'react';
import Navbar from "./Navbar.js";
import Button from "./Button.js";
import Footer from "./Footer.js";
import "./style/Home.css";
import { Link } from 'react-router-dom';



function Home(){
    const items = [
        {id: 1, title: "1. Fill out the form", img: "./static/media/form.png"},
        {id: 2, title: "2. Generate your CV", img: "./static/media/cv.png"},
        {id: 3, title: "3. Copy the job description", img: "./static/media/job.png"},
        {id: 4, title: "4. Generate application letter", img: "./static/media/generate.png"}
    ];

  return (
    <div className="box">
      <Navbar />
      <div className="home-header d-flex flex-column justify-content-center">
        <div className="content-header">
          <p className="home-header-text col-7 col-md-4 d-flex text-align-center">
            Create your perfect resume in just a few minutes!
            Simply sign up, enter your details, and receive
            a professional document – fast, personalized,
            and free.
          </p>
          <div className="start_button">
            <Button className="col-3" type="button">
              <Link to="/resume" className="header-link no-decoration">Get started</Link>
            </Button>
          </div>
        </div>
      </div>
      <div className="steps main">
        <h2 className="steps_title">So erstellst du mit Name ein Anschreiben</h2>
        <ul className="steps_list col-12 flex-column flex-md-row">
          {items.map(item => {
            const itemStyle = {
            backgroundPosition: 'center',
            display: 'flex',
            alignItems: 'flex-end',
            color: 'white',
            padding: '10px',

          };
          return (
              <li key={item.id} className="item">
                <div className="steps_img">
                    <img style={itemStyle} src={item.img}/>
                </div>
                <p className="steps_text">{item.title}</p>
              </li>
            );
          })}
        </ul>
      <div className="resp_button">
            <Button className="col-3" type="button">
              <Link to="/resume" className="header-link no-decoration">Get started</Link>
            </Button>
          </div>
      </div>
      <Footer />
    </div>
  );
};

export default Home;