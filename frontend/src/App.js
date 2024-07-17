import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleQueryChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post('http://localhost:8000/query', { query });
      setResults(response.data.result);
    } catch (error) {
      setError('Error fetching data. Please try again.');
      console.error('Error fetching data: ', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>ByteGenie Chatbot</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={query}
            onChange={handleQueryChange}
            placeholder="Enter your question"
          />
          <button type="submit">Submit</button>
        </form>
        {loading && <p>Loading...</p>}
        {error && <p>{error}</p>}
        {results.length > 0 && (
          <div>
            <h2>Answer</h2>
            <table>
              <thead>
                <tr>
                  {Object.keys(results[0]).map((key) => (
                    <th key={key}>{key}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {results.map((row, index) => (
                  <tr key={index}>
                    {Object.values(row).map((value, i) => (
                      <td key={i}>{value}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
