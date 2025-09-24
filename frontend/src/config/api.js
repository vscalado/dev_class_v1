// Arquivo para configurações da API
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

export const apiConfig = {
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json'
    }
};

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