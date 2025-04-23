import React, { useState } from 'react';
import { postRiskScore } from '../services/api';

const RiskForm = () => {
  const [formData, setFormData] = useState({ age: '', income: '' });
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await postRiskScore(formData);
    setResult(response);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Age:
          <input type="number" name="age" value={formData.age} onChange={handleChange} />
        </label>
        <label>
          Income:
          <input type="number" name="income" value={formData.income} onChange={handleChange} />
        </label>
        <button type="submit">Submit</button>
      </form>
      {result && (
        <div>
          <h3>Risk Score: {result.score}</h3>
          <ul>
            {result.reasons.map((reason, index) => (
              <li key={index}>{reason}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default RiskForm;