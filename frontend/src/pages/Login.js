import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from '../services/api';
import { endpoints } from '../config/api';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      // Criando o FormData conforme esperado pela API
      const formData = new FormData();
      formData.append('username', email); // API espera 'username' mesmo sendo email
      formData.append('password', password);

      // Chamada à API para login
      const response = await api.post(endpoints.login, formData, {
        headers: {
          'Content-Type': 'multipart/form-data', // Importante para FormData
        },
      });

      // Se o login foi bem-sucedido
      if (response.data.access_token) {
        // Salva o token no localStorage
        localStorage.setItem('token', response.data.access_token);
        // Redireciona para o dashboard
        navigate('/dashboard');
      }
    } catch (err) {
      // Tratamento de erros
      const errorMessage = err.response?.data?.detail || 'Erro ao tentar fazer login. Tente novamente.';
      setError(errorMessage);
    }
  };

  return (
    <div className="form-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-field">
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-field">
          <input
            type="password"
            placeholder="Senha"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error && <div className="error-message">{error}</div>}
        <button type="submit" className="button">Entrar</button>
      </form>
      <p>
        Não tem uma conta? <Link to="/register">Cadastre-se</Link>
      </p>
    </div>
  );
}

export default Login;