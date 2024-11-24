import React, { useState } from 'react';

const App = () => {
  const [output, setOutput] = useState(null);
  const [error, setError] = useState(null);

  const handleRunScript = async () => {
    try {
      // Make an API call to the backend
      const response = await fetch('/backend');
      const data = await response.json();

      // Check for error in the response
      if (data.error) {
        setError(data.error);
      } else {
        setOutput(data.output);
      }
    } catch (err) {
      setError('Error occurred while fetching data');
    }
  };

  return (
    <div>
      <button onClick={handleRunScript}>Run Script</button>
      {error && <div style={{ color: 'red' }}>Error: {error}</div>}
      {output && <div>Output: {output}</div>}
    </div>
  );
};

export default App;
