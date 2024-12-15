import React from 'react';
import "./Button.css";
import { Link } from 'react-router-dom';

function Button({ children, style, colSize, colNumber }){
  const buttonClass = `btn ${colSize}-${colNumber}`;
  /*const buttonClass = `btn ${colSm ? `col-sm-${colSm}` : ''} ${colMd ? `col-md-${colMd}` : ''} ${colLg ? `col-lg-${colLg}` : ''}`;*/
    return (
        <button type="button" className={`button ${buttonClass}`} style={style}>
            {children}
        </button>
    );
};

export default Button;