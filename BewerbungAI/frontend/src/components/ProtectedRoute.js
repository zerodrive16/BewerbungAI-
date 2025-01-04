// src/ProtectedRoute.js

import React from 'react';
import { Route, Navigate } from 'react-router-dom'; // Import Navigate instead of Redirect
import { getKeycloak } from './KeycloakService.js'; // Ensure you have a keycloakService.js for initializing Keycloak

// ProtectedRoute component to wrap around protected pages
function ProtectedRoute({ component: Component, ...rest }) {
  const keycloak = getKeycloak(); // Get the Keycloak instance

  return (
    <Route
      {...rest}
      element={keycloak?.authenticated ? <Component /> : <Navigate to="/" />} // Use Navigate for redirection in v6
    />
  );
}

export default ProtectedRoute;
