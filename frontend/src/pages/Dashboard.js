import React, { useState } from 'react';

function Dashboard() {
  const [selectedConverter, setSelectedConverter] = useState(null);

  const converters = [
    { id: 'length', title: 'Comprimento', description: 'Converta entre metros, centímetros, polegadas...' },
    { id: 'volume', title: 'Volume', description: 'Converta entre litros, mililitros, galões...' },
    { id: 'weight', title: 'Peso', description: 'Converta entre quilos, gramas, libras...' },
    { id: 'temperature', title: 'Temperatura', description: 'Converta entre Celsius, Fahrenheit, Kelvin...' }
  ];

  return (
    <div className="dashboard">
      <h1>Bem-vindo ao Portal de Conversores</h1>
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
    </div>
  );
}

export default Dashboard;