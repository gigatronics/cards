export const postRiskScore = async (data) => {
    const response = await fetch('http://localhost:5000/api/risk-score', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    return response.json();
  };