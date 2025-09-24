const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();

// Middlewares
app.use(cors());
app.use(express.json());

// Rota básica de teste
app.get('/api/test', (req, res) => {
  res.json({ message: 'API funcionando!' });
});

// Rotas de autenticação (serão implementadas depois)
app.use('/api/auth', require('./routes/auth'));

// Rotas de conversores (serão implementadas depois)
app.use('/api/converters', require('./routes/converters'));

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});