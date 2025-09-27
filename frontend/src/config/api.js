// Arquivo para configurações da API
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

console.log('=== DEBUG API CONFIG ===');
console.log('Environment variable REACT_APP_API_URL:', process.env.REACT_APP_API_URL);
console.log('Final API_BASE_URL:', API_BASE_URL);

export const apiConfig = {
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json'
    }
};

console.log('Exported apiConfig:', apiConfig);

export const endpoints = {
    register: '/auth/register',
    login: '/auth/login',
    converters: {
        length: '/converters/length',
        volume: '/converters/volume',
        weight: '/converters/weight',
        temperature: '/converters/temperature'
    }
};

console.log('Endpoints:', endpoints);
console.log('=== END DEBUG API CONFIG ===');