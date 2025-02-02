import { useState, useEffect } from 'react';
import axios from 'axios';

const useCSRFToken = () => {
  const [csrfToken, setCsrfToken] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCSRFToken = async () => {
      const match = document.cookie.match(new RegExp('(^| )csrftoken=([^;]+)'));
      if (match) {
        return match[2]; // Return the CSRF token from the cookie
      }
      try {
        const response = await axios.get('http://127.0.0.1:8000/get-csrf-token', {
          withCredentials: true, // Ensure cookies are included
        });

        // Check if csrfToken exists in response
        if (response.data && response.data.csrfToken) {
          const token = response.data.csrfToken;
          setCsrfToken(token);
          sessionStorage.setItem('csrfToken', token); // Store in sessionStorage
          axios.defaults.headers['X-CSRFToken'] = token; // Set as global Axios header
        } else {
          throw new Error('CSRF token not found in response');
        }
      } catch (err) {
        setError(err.message || 'Failed to fetch CSRF token');
        console.error('Error fetching CSRF token:', err);
      }
    };

    fetchCSRFToken();
  }, []);

  return { csrfToken, error };
};

export default useCSRFToken;