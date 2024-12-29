import React from "react";
import "./InputForm.css";


function InputForm({ label, type, name, value, onChange, customStyles, ...rest }) {
  return (
    <div className="input-form" >
      <input className="input"
        type={type}
        name={name}
        value={value}
        placeholder={label}
        style={customStyles}
        onChange={onChange}
      />
    </div>
  );
}

export default InputForm;
