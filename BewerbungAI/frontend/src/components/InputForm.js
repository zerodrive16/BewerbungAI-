import React from "react";
import "./style/InputForm.css";
import { useState, useEffect,  } from 'react';



function InputForm({
  label,
  type = "text",
  name,
  value,
  onChange,
  customStyles,
  colNumber,
  inputClass,
  maxLength,
  pattern,
  errorMessage
  }) {

  return (
    <div className="input-form">
      <input className=""
        type={type}
        name={name}
        value={value}
        placeholder={label}
        style={customStyles}
        onChange={onChange}
        className={`input ${inputClass}`}
        maxLength={maxLength}
        pattern={pattern}
        required
      />
    </div>
  );
}

export default InputForm;
