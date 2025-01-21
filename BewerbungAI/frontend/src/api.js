import axios from 'axios';

// Function to export users to Django from Keycloak
export const exportUsersToDjango = async (token) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/export-users/', {}, {
      headers: {
        'Authorization': `Bearer ${token}`, // Use the Keycloak token
        'X-CSRFToken': sessionStorage.getItem('csrfToken'), // Include CSRF token if needed
      },
    });

    return response.data; // Return response for further handling
  } catch (error) {
    console.error('Failed to export users:', error);
    throw error; // Re-throw to handle it in the component if needed
  }
};