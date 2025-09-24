import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from '../services/api';
import { endpoints } from '../config/api';

function Register() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Validações básicas
    if (formData.password !== formData.confirmPassword) {
      setError('As senhas não coincidem');
      return;
    }

    try {
      // Removendo confirmPassword antes de enviar
      const { confirmPassword, ...registrationData } = formData;
      
      // Chamada à API para registro
      const response = await api.post(endpoints.register, registrationData);
      
      // Se o registro foi bem-sucedido
      if (response.data.access_token) {
        // Salva o token no localStorage
        localStorage.setItem('token', response.data.access_token);
        // Redireciona para o dashboard
        navigate('/dashboard');
      }
    } catch (err) {
      // Tratamento de erros
      const errorMessage = err.response?.data?.detail || 'Erro ao tentar cadastrar. Tente novamente.';
      setError(errorMessage);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div className="form-container">
      <h2>Cadastro</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-field">
          <input
            type="text"
            name="name"
            placeholder="Nome completo"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-field">
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-field">
          <input
            type="password"
            name="password"
            placeholder="Senha"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-field">
          <input
            type="password"
            name="confirmPassword"
            placeholder="Confirmar senha"
            value={formData.confirmPassword}
            onChange={handleChange}
            required
          />
        </div>
        {error && <div className="error-message">{error}</div>}
        <button type="submit" className="button">Cadastrar</button>
      </form>
      <p>
        Já tem uma conta? <Link to="/">Faça login</Link>
      </p>
    </div>
  );
}

export default Register;