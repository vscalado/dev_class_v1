import axios from 'axios';
import { apiConfig } from '../config/api';

console.log('=== DEBUG API SERVICE ===');
console.log('API Config loaded:', apiConfig);
console.log('Base URL from config:', apiConfig.baseURL);

const api = axios.create(apiConfig);

// Interceptor para debug das requisições
api.interceptors.request.use((config) => {
    console.log('=== MAKING API REQUEST ===');
    console.log('Request URL:', config.baseURL + config.url);
    console.log('Request method:', config.method);
    console.log('Request data:', config.data);
    console.log('Full request config:', config);
    
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
        console.log('Token added to request');
    } else {
        console.log('No token found in localStorage');
    }
    
    console.log('=== END API REQUEST DEBUG ===');
    return config;
});

// Interceptor para debug das respostas
api.interceptors.response.use(
    (response) => {
        console.log('=== API RESPONSE SUCCESS ===');
        console.log('Response status:', response.status);
        console.log('Response data:', response.data);
        console.log('=== END API RESPONSE ===');
        return response;
    },
    (error) => {
        console.log('=== API RESPONSE ERROR ===');
        console.log('Error status:', error.response?.status);
        console.log('Error data:', error.response?.data);
        console.log('Error message:', error.message);
        console.log('Full error:', error);
        console.log('=== END API ERROR ===');
        return Promise.reject(error);
    }
);

console.log('=== API SERVICE INITIALIZED ===');

export default api;