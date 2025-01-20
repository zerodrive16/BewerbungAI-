
// ProtectedRoute.js
import React from 'react';
import { Route, Navigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

const ProtectedRoute = ({ element }) => {
    const { kc } = useAuth();

    // If the user is not authenticated, redirect to the login page
    if (!kc.authenticated) {
        kc.login();
        return null;
    }

    return element; // Render the protected element
};
export default ProtectedRoute;