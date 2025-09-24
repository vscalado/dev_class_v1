import React, { useState } from 'react';
import api from '../services/api';
import { endpoints } from '../config/api';

function Converter({ type, units }) {
  const [formData, setFormData] = useState({
    value: '',
    from_unit: units[0],
    to_unit: units[1]
  });
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await api.post(endpoints.converters[type], {
        value: parseFloat(formData.value),
        from_unit: formData.from_unit,
        to_unit: formData.to_unit
      });

      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Erro ao realizar a conversão. Tente novamente.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="converter-component">
      <form onSubmit={handleSubmit}>
        <div className="form-row">
          <div className="form-field">
            <input
              type="number"
              name="value"
              value={formData.value}
              onChange={handleChange}
              placeholder="Valor"
              required
              step="any"
            />
          </div>
          <div className="form-field">
            <select 
              name="from_unit" 
              value={formData.from_unit}
              onChange={handleChange}
              required
            >
              {units.map(unit => (
                <option key={unit} value={unit}>{unit}</option>
              ))}
            </select>
          </div>
          <div className="form-field">
            <span>para</span>
          </div>
          <div className="form-field">
            <select 
              name="to_unit" 
              value={formData.to_unit}
              onChange={handleChange}
              required
            >
              {units.map(unit => (
                <option key={unit} value={unit}>{unit}</option>
              ))}
            </select>
          </div>
        </div>
        <button 
          type="submit" 
          className="button"
          disabled={loading}
        >
          {loading ? 'Convertendo...' : 'Converter'}
        </button>
      </form>

      {error && <div className="error-message">{error}</div>}
      
      {result && (
        <div className="result">
          <h3>Resultado:</h3>
          <p>
            {result.original_value} {result.from} = {result.result} {result.to}
          </p>
        </div>
      )}
    </div>
  );
}

export default Converter;