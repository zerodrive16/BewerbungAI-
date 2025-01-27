import React from 'react';
import "./style/Button.css";
import { Link } from 'react-router-dom';

function Button({onClick, type, children, style, col, colMd}){
  //const buttonClass = `btn ${colSize}-${colNumber}`;
  const buttonClass = `btn ${col ? `col-${col}` : ''} ${colMd ? `col-md-${colMd}` : ''}`;
    return (
        <button onClick={onClick} type={type} className={`button ${buttonClass}`} style={style}>
            {children}
        </button>
    );
};

export default Button;