import React from "react";
import "./InputForm.css";
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
  errorMessage
  }) {
  const [error, setError] = useState("");
  const handleValidation = (e) => {
    const { value } = e.target;
    if (maxLength && value.length > maxLength) {
      setError(`Must be ${maxLength} characters or less.`);
      return;
    }
    setError("");
  }

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
        required
      />
      {error && <p className="error-message">{error}</p>}
    </div>
  );
}

export default InputForm;
