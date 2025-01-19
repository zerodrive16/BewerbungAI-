import React from 'react';
import "./style/Button.css";
import { Link } from 'react-router-dom';

function Button({onClick, type, children, style, colSize, colNumber }){
  const buttonClass = `btn ${colSize}-${colNumber}`;
  /*const buttonClass = `btn ${colSm ? `col-sm-${colSm}` : ''} ${colMd ? `col-md-${colMd}` : ''} ${colLg ? `col-lg-${colLg}` : ''}`;*/
    return (
        <button onClick={onClick} type={type} className={`button ${buttonClass}`} style={style}>
            {children}
        </button>
    );
};

export default Button;