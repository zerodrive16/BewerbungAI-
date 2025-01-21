import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
   <App />
);

//import React from 'react';
//import ReactDOM from 'react-dom/client';
//import { BrowserRouter } from 'react-router-dom';
//import { AuthProvider } from './AuthContext';
//import App from './App';
//
//const root = ReactDOM.createRoot(document.getElementById('root'));
//root.render(
//    <BrowserRouter>
//        <AuthProvider>
//            <App />
//        </AuthProvider>
//    </BrowserRouter>
//);