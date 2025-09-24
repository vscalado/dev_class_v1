import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Converter from '../components/Converter';
import { UNITS, CONVERTER_TITLES } from '../constants/units';

function Dashboard() {
  const [selectedConverter, setSelectedConverter] = useState(null);
  const navigate = useNavigate();

  // Verificar autenticação
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/');
    }
  }, [navigate]);

  const converters = [
    { id: 'length', title: 'Comprimento', description: 'Converta entre metros, centímetros, quilômetros...' },
    { id: 'volume', title: 'Volume', description: 'Converta entre litros, mililitros, metros cúbicos...' },
    { id: 'weight', title: 'Peso', description: 'Converta entre quilos, gramas, libras...' },
    { id: 'temperature', title: 'Temperatura', description: 'Converta entre Celsius, Fahrenheit, Kelvin...' }
  ];

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/');
  };

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>Portal de Conversores</h1>
        <button onClick={handleLogout} className="button logout-button">
          Sair
        </button>
      </header>

      {selectedConverter ? (
        <div className="converter-section">
          <button 
            className="button back-button"
            onClick={() => setSelectedConverter(null)}
          >
            Voltar
          </button>
          <h2>{CONVERTER_TITLES[selectedConverter]}</h2>
          <Converter 
            type={selectedConverter}
            units={UNITS[selectedConverter]}
          />
        </div>
      ) : (
        <div className="converter-grid">
          {converters.map(converter => (
            <div key={converter.id} className="converter-card">
              <h3>{converter.title}</h3>
              <p>{converter.description}</p>
              <button 
                className="button"
                onClick={() => setSelectedConverter(converter.id)}
              >
                Abrir
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Dashboard;