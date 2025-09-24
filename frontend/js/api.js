// Configurações da API
const API_URL = '/api/'; // Adicionada a barra no final

// Funções auxiliares para chamadas à API
async function apiCall(endpoint, method = 'GET', data = null) {
    // Remove a barra inicial do endpoint se existir
    const cleanEndpoint = endpoint.startsWith('/') ? endpoint.slice(1) : endpoint;
    const url = `${API_URL}${endpoint}`;
    console.log(`Fazendo chamada ${method} para: ${url}`);
    if (data) {
        console.log('Dados enviados:', data);
    }

    const options = {
        method,
        headers: {
            'Content-Type': 'application/json'
        }
    };

    // Adiciona o token de autenticação se existir
    const token = localStorage.getItem('token');
    if (token) {
        options.headers['Authorization'] = `Bearer ${token}`;
    }

    // Adiciona o corpo da requisição se houver dados
    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        console.log('Opções da requisição:', options);
        const response = await fetch(url, options);
        
        let result;
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.includes("application/json")) {
            result = await response.json();
        } else {
            result = await response.text();
            console.warn('Resposta não é JSON:', result);
        }

        if (!response.ok) {
            console.error('Erro na API:', {
                status: response.status,
                statusText: response.statusText,
                result
            });
            
            // Trata diferentes tipos de respostas de erro
            let errorMessage = 'Erro na requisição';
            if (result) {
                if (result.detail) {
                    errorMessage = result.detail;
                } else if (typeof result === 'string') {
                    errorMessage = result;
                } else if (result.message) {
                    errorMessage = result.message;
                }
            }
            throw new Error(errorMessage);
        }

        console.log('Resposta da API:', result);
        return result;
    } catch (error) {
        console.error('Erro detalhado na API:', error);
        throw error;
    }
}