import Keycloak from 'keycloak-js';

let keycloak = null;

export const initKeycloak = (onAuthenticatedCallback) => {
  keycloak = new Keycloak({
    url: 'http://localhost:8080/auth',  // Keycloak server URL
    realm: 'myrealm',
    clientId: 'react-client',
  });

  keycloak.init({
    onLoad: 'login-required',
    checkLoginIframe: false,  // Disable iframe login check to avoid issues
  }).then((authenticated) => {
    if (authenticated) {
      console.log("Authenticated");
      onAuthenticatedCallback();
    } else {
      console.log("Not authenticated");
    }
  }).catch((error) => {
    console.log("Failed to initialize Keycloak", error);
  });
};

export const getKeycloak = () => keycloak;
