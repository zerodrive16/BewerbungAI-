import React from "react";
import "./InputForm.css";


function InputForm({ label, type, name, value, onChange, customStyles, colNumber }) {
  const inputClass = `col-${colNumber}`;
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
      />
    </div>
  );
}

export default InputForm;
